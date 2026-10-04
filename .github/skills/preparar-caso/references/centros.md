# Cómo publica cada centro los documentos de calidad

Patrones observados en las webs de los centros (WordPress). Sirven para ir directo a las
páginas; compruébalos siempre con `evaluacion.py enlaces`, porque las webs cambian.

## Escuela Superior de Ingeniería (ESI) — `esingenieria.uca.es`

- Página del título: `/docencia/grados/<siglas>/` (másteres: `/docencia/masteres/<slug>/`).
- `/docencia/grados/<siglas>/informes/`: autoinformes de seguimiento y de renovación,
  planes de mejora e informes de la agencia (enlaces «Autoinforme», «Plan de mejora»,
  «Informe ACCUA», «Informe DEVA», «Informe»), por curso.
- `/docencia/grados/<siglas>/datos-generales/`: «Memoria», «Informe de verificación»,
  «Informe de modificación» y RUCT.
- Particularidad: solo se publica la memoria en vigor, con el año en el nombre del fichero;
  puede ser posterior al curso del caso.
- Índice de todos los títulos: `/calidad/rendicion-de-cuentas/`.

## Facultad de Filosofía y Letras (FFL) — `filosofia.uca.es`

- Página del título: `/estudios/grados/<slug>/` (másteres: `/estudios/masteres/<slug>/`).
  Todo está en esa página, en desplegables: «Autoinformes de seguimiento», «Informes de
  seguimiento», «Informes de renovación de la acreditación», «Memoria en vigor» e
  «Informe de verificación».
- Particularidades: los nombres de fichero son heterogéneos (algunos acaban en
  `_redacted`) y algunos enlaces apuntan a una página intermedia de WordPress que redirige
  al PDF (el script la sigue).
- Los «Informes de seguimiento» incluyen tanto informes de la agencia como seguimientos del
  plan de mejora: distínguelos por el nombre del fichero o la portada.
