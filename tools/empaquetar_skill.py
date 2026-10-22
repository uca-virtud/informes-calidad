"""Empaqueta la skill en dist/uca-informes-calidad.zip para subirla a Claude.

Uso: python3 tools/empaquetar_skill.py

El zip es reproducible: con la misma skill produce el mismo fichero, así que
solo cambia en Git cuando cambia la skill.
"""
import pathlib
import zipfile

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SKILL = RAIZ / 'skills' / 'uca-informes-calidad'
DESTINO = RAIZ / 'dist' / 'uca-informes-calidad.zip'
EXCLUIDOS = {'__pycache__', '.DS_Store'}
FECHA_FIJA = (2026, 1, 1, 0, 0, 0)


def ficheros_de_la_skill():
    return sorted(
        ruta for ruta in SKILL.rglob('*')
        if ruta.is_file() and not EXCLUIDOS.intersection(ruta.relative_to(SKILL).parts)
    )


def main():
    DESTINO.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(DESTINO, 'w', zipfile.ZIP_DEFLATED) as zip_skill:
        for ruta in ficheros_de_la_skill():
            entrada = zipfile.ZipInfo(ruta.relative_to(SKILL.parent).as_posix(), FECHA_FIJA)
            entrada.compress_type = zipfile.ZIP_DEFLATED
            entrada.external_attr = 0o644 << 16
            zip_skill.writestr(entrada, ruta.read_bytes())
    print(f'Generado {DESTINO.relative_to(RAIZ)}')


if __name__ == '__main__':
    main()
