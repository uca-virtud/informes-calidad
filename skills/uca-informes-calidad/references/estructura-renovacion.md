# Estructura del Autoinforme de Renovación de la Acreditación (ACCUA – UCA)

La renovación de la acreditación se presenta en la **plataforma web de ACCUA**, no como
un Word. Para no redactar directamente en la plataforma, la Unidad de Calidad facilita
una plantilla `.docx` **por criterio** (`assets/plantillas_renovacion/*CRITERIO_n*.docx`,
formato "GyM" para grados y másteres). La coordinación prepara ahí el texto y luego lo
vuelca en la plataforma.

## Entregables de la skill

- `Criterio_1.docx` … `Criterio_7.docx`: cada plantilla con la parte determinista
  rellena (`scripts/rellenar_renovacion.py`) y el análisis redactado.
- `Anexo_I_Indicadores.docx`: tablas ISGC P01–P07 por TÍTULO y por CENTRO. Las
  plantillas de renovación no traen estas tablas; el script las toma del Anexo 1 de
  `assets/plantilla_autoinforme_seguimiento.docx` (mismo formato y columnas de años). Las etiquetas de los indicadores contienen
  "Título-Centro"; el ámbito TÍTULO/CENTRO de una tabla solo se lee en sus filas de
  cabecera (las que no llevan código ISGC).

Los Anexos II (personal académico), III (prácticas externas, lo aporta el centro) y IV
(calificaciones) se citan en los criterios como enlaces a la web del título o a UCADrive.

## Diferencias con el seguimiento

| Aspecto | Seguimiento | Renovación |
|---|---|---|
| Periodo analizado | El curso del autoinforme, con su evolución | **Todo el periodo de acreditación** (cursos desde la última renovación) |
| Documento | Un `.docx` con anexos y plan de mejora | 7 `.docx` por criterio + Anexo I |
| Puntos fuertes | Solo los del curso | Los del presente autoinforme **y** los de los autoinformes del periodo, agrupados por curso |
| Puntos débiles | Punto débil → acción | `Autoinforme del curso | Punto débil | Propuestas de mejora | Impacto (causa-efecto)` |
| Criterio 2.4 | Tabla de recomendaciones del último informe ACCUA | Análisis de los planes de mejora del periodo + dos tablas de recomendaciones con evidencia e impacto |
| Plan de mejora final | Sí | No: se valora el impacto de las acciones del periodo |
| Evidencias | Solo si va a ACCUA | Siempre: bloques "Evidencias según guía ACCUA" y enlaces a UCADrive |

## Documentos que hay que pedir al usuario

Además de la **memoria verificada** (objetivos de las tasas, plazas, modalidad):

- **Todos los autoinformes de seguimiento del periodo** — *clave*. Aportan los puntos
  fuertes y débiles por curso, las acciones de mejora y sus códigos (`PF/PD/AM-…`).
- **Último informe de renovación de ACCUA** e **informes de seguimiento de ACCUA del
  periodo** — *clave*. Alimentan las dos tablas del subcriterio 2.4.
- **Informes de modificación del título** del periodo (fecha y recomendaciones), si los hay.
- **Enlaces a evidencias en UCADrive/Colabora** (actas de la CGC, auditoría de la IPD,
  rúbricas y listados de TFG/TFM, memorias de prácticas, personal de apoyo…).

Lo que falte se marca como `[PENDIENTE: …]`, igual que en el seguimiento.

## Estructura de cada plantilla

Todas empiezan con el título "Autoinforme Global de Renovación de la Acreditación de los
Títulos Oficiales", la línea "Formato para la redacción del Criterio n. GyM" (la elimina
`rellenar_renovacion.py`) y el convenio de colores (negro: propuesta de redacción;
rojo: instrucciones; azul: directrices de ACCUA).

- **Criterio 1** abre con la ficha de identificación (12 campos). Claves exactas para
  `identificacion` en el JSON: `Universidad`, `ID Ministerio`, `Denominación del título`,
  `Curso académico de implantación`, `Modalidad de enseñanza (presencial, híbrida o
  virtual)`, `En su caso, créditos prácticos obligatorios`, `Centro o centros donde se
  imparte el título`, `En caso de ser un título conjunto, universidades donde se imparte`,
  `En su caso, anteriores convocatorias de renovación de acreditación`, `En caso de
  títulos dobles, especificar la titulación y la universidad`, `En su caso, estructuras
  curriculares específicas`, `Web del título`.
- **Criterios 2–7** abren con `Denominación del título` (misma clave).

Cada criterio termina con la tabla de **Puntos fuertes y/o logros** y la de **Puntos
débiles y decisiones de mejora adoptadas**.

### Subcriterios

Los mismos enunciados que en el seguimiento (ver `estructura-autoinforme.md`), con
encabezado "Subcriterio n.m:":

- **I. Información pública disponible**: 1.1 información del programa y su desarrollo
  operativo; 1.2 resultados y satisfacción publicados; 1.3 SGC y resultados de las
  revisiones publicados; 1.4 satisfacción con la IPD (ISGC-P01-01 a 03). Incluir en
  UCADrive los resultados de la auditoría de la IPD.
- **II. Sistema de Garantía de la Calidad**: 2.1 responsables y política de calidad;
  2.2 procedimiento de diseño, revisión y mejora (incluye títulos interuniversitarios);
  2.3 recogida de información y satisfacción; **2.4 plan de mejora**, con tres apartados:
  1. *Plan de mejora*: análisis de los planes de mejora del periodo y de su influencia
     en el título (causa-efecto). Tabla con las recomendaciones **resueltas** del último
     informe de renovación que no aparezcan ya en el último informe de seguimiento.
  2. *Modificaciones para la mejora del título*: fecha del informe de modificación de
     ACCUA y sus recomendaciones (misma tabla de tres columnas).
  3. *Acciones ante las recomendaciones del informe de seguimiento*: **todas** las
     recomendaciones del último informe de seguimiento de ACCUA, por convocatoria.
- **III. Diseño, organización y desarrollo del programa formativo**: 3.1–3.6. En 3.3,
  reconocimientos de créditos agregados de todo el periodo; en 3.4, ISGC-P04-16 a 19 y
  el informe "P04 – Perfil de Ingreso – ACCUA" como evidencia; en 3.5, ISGC-P04-10.
- **IV. Profesorado**: 4.1–4.8 (4.8 = satisfacción del profesorado, ISGC-P07-03).
- **V. Recursos y apoyo a la docencia**: 5.1–5.4 (no hay 5.5). Tabla `Nombre evidencia |
  Enlace evidencia` al final.
- **VI. Resultados del programa formativo**: 6.1–6.4. Evidencias: cinco asignaturas
  representativas (incluido TFG/TFM y prácticas), listado y rúbrica de TFG/TFM,
  calificaciones (Anexo IV) y resultados de primer curso de los últimos seis años.
- **VII. Orientación académica, profesional y empleabilidad**: 7.1–7.6. El 7.6
  (sostenibilidad) resume las conclusiones de los criterios 3 a 6.

## Cómo redactar lo específico de la renovación

- **Analiza el periodo completo**: evolución de cada indicador en todos los cursos del
  Anexo I, no solo el último. Apóyate en los autoinformes del periodo.
- **Puntos fuertes**: agrupa por curso (`2020/21:`, `2021/22:`…) respetando el código
  original de cada autoinforme; añade los del presente autoinforme en el último curso.
- **Puntos débiles**: una fila por punto débil y curso. En *Impacto*, cita el indicador
  del SGC y su serie de valores (p. ej. `ISGC-P01-01: 20/21: 3,25 · … · 24/25: 3,37`) o
  el hecho verificable que demuestra el efecto de la acción.
- **Recomendaciones**: copia literal del informe de ACCUA; en *Acciones* indica la acción
  y la evidencia contrastable (ruta o enlace); en *Impacto*, el efecto observado o
  esperado.
- **Evidencias**: sustituye cada bloque azul "Evidencias según guía ACCUA" por enlaces
  reales, o `[PENDIENTE: subir a UCADrive …]`.

## Esquema del JSON de datos (`rellenar_renovacion.py`)

Ejemplo completo en `assets/ejemplo_datos_renovacion.json`. `anios`, `anios_egresados`,
`extraccion` e `indicadores` siguen el esquema y las reglas de la serie histórica de
`mapa-indicadores-lincebi.md`.

```json
{
  "tipo": "renovacion",
  "identificacion": {"Denominación del título": "…", "ID Ministerio": "…"},
  "anios": ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"],
  "anios_egresados": ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
  "extraccion": {"entorno": "data.uca.es", "fecha": "2026-03-01"},
  "indicadores": {"ISGC-P04-01": {"titulo": {"2024-25": "81,2"}, "centro": {}}},
  "puntos": {
    "1": {
      "fuertes": {"2023/24": ["PF-…"], "2024/25": ["PF-…"]},
      "debiles": [{"curso": "2020/21", "punto": "PD-…", "propuestas": "AM-…", "impacto": "ISGC-…"}]
    }
  },
  "recomendaciones_renovacion": [{"rec": "…", "accion": "…", "evidencia": "…", "impacto": "…"}],
  "recomendaciones_seguimiento": [{"convocatoria": "Convocatoria 22/23", "rec": "…", "accion": "…", "evidencia": "…", "impacto": "…"}],
  "evidencias": {"5": [{"nombre": "Listado del personal de apoyo", "enlace": "…"}]}
}
```

`fuertes` también admite una lista simple (sin agrupar por curso). Las tablas sin datos
en el JSON se dejan como en la plantilla para completarlas a mano. Las filas que falten
se añaden copiando el formato de la primera fila de datos, y las filas de ejemplo
sobrantes se eliminan.

## Checklist final de la renovación

1. Ficha de identificación completa (criterio 1) y denominación en los criterios 2–7.
2. Cada subcriterio analiza el periodo completo y cita los indicadores del Anexo I.
3. Puntos fuertes y débiles de todos los autoinformes del periodo, con su curso; cada
   punto débil con propuesta e impacto.
4. Subcriterio 2.4 con las tablas de recomendaciones completas (último informe de
   renovación, modificaciones y último informe de seguimiento) y su evidencia.
5. Evidencias enlazadas (UCADrive/web) en lugar de los bloques azules.
6. Sin texto rojo/azul, corchetes, `XXXX` ni la línea "Formato para la redacción…".
7. Columnas de años del Anexo I acordes al periodo (el script avisa si faltan).
