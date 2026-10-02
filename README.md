# Informes de calidad — UCA

Automatización asistida de la preparación de informes de calidad de títulos oficiales
de la Universidad de Cádiz.

## Documentación

- [Visión del proyecto](docs/VISION.md): contexto, objetivo y fases.
- [Skill de autoinformes](skills/uca-informes-calidad/SKILL.md): procedimiento de
  elaboración, recursos y criterios de entrega.
- [Evaluaciones](docs/EVALUACIONES.md): resultados de la skill frente a autoinformes
  reales, lecciones aprendidas y su estado.
- [Solicitud de la fase 1 al Sistema de Información](docs/peticiones-cartera/solicitud-SI-fase1.md):
  modelo de datos e informe agregado de indicadores del Anexo I.

## Sitio web del proyecto

El sitio `web/` (MkDocs + Material) difunde el proyecto entre los colectivos implicados de
la UCA. Se publica en GitHub Pages con todas las páginas cifradas con una contraseña
compartida, y no contiene documentos ni datos personales. Se despliega automáticamente al
hacer push a `main` (`.github/workflows/pages.yml`).

Vista previa local:

```bash
python3 -m venv /tmp/venv-web && /tmp/venv-web/bin/pip install -r web/requirements.txt
cd web && SITE_PASSWORD=<contraseña de prueba> /tmp/venv-web/bin/mkdocs serve
```

## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `skills/uca-informes-calidad/` | Skill vigente (seguimiento y renovación de la acreditación). |
| `old-skills/autoinforme-seguimiento-uca/` | Versión anterior de la skill, solo de seguimiento, usada en las evaluaciones. |
| `evals/` | Evaluaciones por título: datos de partida, borrador de la IA, autoinforme humano y cotejo. |
| `samples/` | Autoinformes reales de ejemplo (seguimiento y renovación). |
| `docs/` | Visión del proyecto, evaluaciones, peticiones de cartera de los centros y solicitud de la fase 1 al SI. |
| `web/` | Sitio web del proyecto (MkDocs), publicado en GitHub Pages con contraseña. |