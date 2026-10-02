"""Salvaguardas del sitio: nunca publicar contenido sin cifrar ni documentos del proyecto."""

import os
import posixpath
import re

from mkdocs.exceptions import PluginError

DOCUMENTOS_PROHIBIDOS = ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.zip')
MARCA_CIFRADO = 'id="mkdocs-encrypted-content"'
ENLACE = re.compile(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
EXTERNO = re.compile(r'^(?:[a-z][a-z0-9+.-]*:|#)', re.IGNORECASE)


def on_config(config):
    if not os.environ.get('SITE_PASSWORD', '').strip():
        raise PluginError('Falta la variable de entorno SITE_PASSWORD: el sitio no se genera sin cifrar.')
    return config


def on_page_markdown(markdown, page, config, files):
    """Deja como texto los enlaces que no apuntan a una página del sitio (PDF, DOCX, skill...)."""
    paginas = {f.src_uri for f in files.documentation_pages()}
    origen = posixpath.dirname(page.file.src_uri)

    def resolver(coincidencia):
        texto, destino = coincidencia.groups()
        if EXTERNO.match(destino):
            return coincidencia.group(0)
        ruta = posixpath.normpath(posixpath.join(origen, destino.split('#', 1)[0]))
        return coincidencia.group(0) if ruta in paginas else texto

    return ENLACE.sub(resolver, markdown)


def on_post_page(output, page, config):
    if MARCA_CIFRADO not in output:
        raise PluginError(f'La página {page.file.src_uri} no se ha cifrado.')
    return output


def on_post_build(config):
    for raiz, _, ficheros in os.walk(config['site_dir']):
        for nombre in ficheros:
            if nombre.lower().endswith(DOCUMENTOS_PROHIBIDOS):
                raise PluginError(f'Documento no permitido en el sitio: {os.path.join(raiz, nombre)}')
