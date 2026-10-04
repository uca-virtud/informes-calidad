# Mapa de indicadores ISGC ↔ LinceBI ↔ tablas de la plantilla

Todos los indicadores viven en LinceBI, bajo:
`https://data.uca.es/lincebi/` → `Datos Académicos/Calidad/Indicadores Procesos SGC/`
(requiere VPN/sesión de la UCA). Cada tabla del Anexo 1 se replica para **TÍTULO** y
para **CENTRO**.

En la **renovación**, el Anexo I se genera con estas mismas tablas (las de la plantilla
de seguimiento) mediante `scripts/rellenar_renovacion.py`, así que el mapa y el esquema de
`indicadores` son los mismos.

## Cómo extraer un indicador de LinceBI

1. `lincebi_search_resources(query, types=["REPORT_PRD"])` con palabras clave del
   indicador o de la carpeta (p. ej. "Tasa de rendimiento", "P04", "Difusión de la
   Información", "Encuesta egresados").
2. `lincebi_get_report_parameters(path)` para ver los parámetros. Habitualmente hay que
   fijar el **plan/título** y el **curso académico** (a veces también el centro).
   Resuelve las cascadas pasando `context`.
3. `lincebi_get_report_data(path, parameters, maxRows)` para los datos. La respuesta
   incluye `viewerUrl`: cítala al usuario (avisa de que requiere sesión activa).
4. Repite por cada curso de las columnas (o extrae la serie completa si el informe la
   devuelve).

Si LinceBI no responde (sin VPN), díselo al usuario y usa los archivos que aporte o
deja `[PENDIENTE]`.

## Años de las columnas

- Tablas generales (P01, P04, P05, P06, P07 satisfacción/BAU): los **5 cursos** más
  recientes. Para la convocatoria 2026 (curso 2024/25): `2020-21, 2021-22, 2022-23,
  2023-24, 2024-25`.
- Tablas de **egresados** (P07-01_03, P07-05 a 10): por **año de egreso**. Usa las
  **cinco últimas cohortes con datos en LinceBI**, aunque la plantilla traiga otras. Para
  la convocatoria 2026: `2019-20 … 2023-24`. Comprueba en LinceBI cuál es la última
  cohorte encuestada; si aún no tiene datos, desplaza la ventana un año atrás y avísalo.
- Resultados globales de las tasas (criterio 6): se piden los **últimos seis años**, uno
  más que la ventana de LinceBI. El curso más antiguo se toma del autoinforme anterior,
  citándolo como fuente.

`rellenar_autoinforme.py` sustituye los años de las cabeceras de la plantilla por los de
`anios` y `anios_egresados` del JSON, así que basta con fijarlos ahí.

## Regla de la serie histórica

- **Extrae toda la serie en vivo** de LinceBI, también los cursos que ya figuran en el
  autoinforme anterior: la coordinación prioriza el dato vigente sobre la continuidad con
  el documento anterior.
- Usa el autoinforme anterior **solo** para: (a) columnas que LinceBI ya no muestra por la
  ventana móvil de cinco cursos (p. ej. columnas de centro antiguas y el sexto curso de
  resultados globales del criterio 6) y (b) indicadores cuyo valor vivo es incoherente
  (p. ej. fuera de escala). Indícalo en el análisis.
- **Registra el entorno y la fecha** de extracción en el bloque `extraccion` del JSON y
  menciónalos al usuario. Las tasas son dinámicas: la **tasa de graduación (P04-05)** puede
  variar varios puntos en pocos meses. Si hay que comparar con un documento ya aprobado,
  avisa de que la diferencia puede deberse a la fecha de extracción.

## Comprobaciones de coherencia

- Los indicadores de satisfacción están en **escala 0-5**: ningún valor puede superar 5
  (el script avisa si ocurre). Un valor mayor indica un dato sin normalizar.
- Las tablas de egresados de título y de centro deben usar la **misma alineación
  cohorte-valor**: cada valor va en la columna de su año de egreso.
- En **P07-01_03** (tasa de respuesta de egresados) anota junto al porcentaje el número de
  encuestas y de egresados, p. ej. `29,55% (13/44)`.

## Correspondencia tabla → indicadores

Rutas relativas a `Datos Académicos/Calidad/Indicadores Procesos SGC/`.

### T27 (TÍTULO) / T28 (CENTRO) — P01 Difusión de la Información
Ruta: `P01 - Proceso de Reparto de la Información/P01 - Indicador Difusión de la Información`
- ISGC-P01-01 Satisfacción del alumnado con la información publicada
- ISGC-P01-02 Satisfacción del PDI con la información publicada
- ISGC-P01-03 Satisfacción del PTGAS con la información publicada del Centro

### T29 (TÍTULO) / T30 (CENTRO) — P04 Enseñanza-Aprendizaje (rendimiento y satisfacción)
Ruta: `P04 - Gest. Procesos de Enseñanza-Aprendizaje/`
- ISGC-P04-01 Tasa de rendimiento (%)
- ISGC-P04-02 Tasa de éxito (%)
- ISGC-P04-03 Tasa de evaluación / presentados (%)
- ISGC-P04-04 Tasa de abandono (%)
- ISGC-P04-05 Tasa de graduación (%)
- ISGC-P04-06 Tasa de eficiencia (%)
- ISGC-P04-07 Duración media de los estudios
- ISGC-P04-08 Plazas de prácticas externas / alumnado que las solicita
- ISGC-P04-09 % alumnado en movilidad → 4 filas: entrante internacional, entrante
  nacional, saliente internacional, saliente nacional
- ISGC-P04-10 Satisfacción del alumnado con la coordinación docente
- ISGC-P04-11 Satisfacción del alumnado con elección/realización del TFG/TFM
- ISGC-P04-12 Satisfacción de tutores académicos con prácticas externas
- ISGC-P04-13 Satisfacción de tutores de entidades colaboradoras con el desempeño
- ISGC-P04-14 Satisfacción del alumnado con las prácticas externas
- ISGC-P04-15 Satisfacción del alumnado con redes de movilidad (entrante/saliente)

### T31 (TÍTULO) / T32 (CENTRO) — P05 Personal Docente
Ruta: `P05 - Gest. Personal Docente/`
- ISGC-P05-02 Participación del profesorado en acciones formativas (%)
- ISGC-P05-03 Participación en proyectos de innovación y mejora docente (%)
- ISGC-P05-04 Satisfacción global de los estudiantes con la docencia
- ISGC-P05-05 % profesores en convocatorias DOCENTIA (%)
- ISGC-P05-06 % calificaciones "EXCELENTES" en DOCENTIA (%)
- ISGC-P05-07 % calificaciones "FAVORABLE" en DOCENTIA (%)

### T33 (TÍTULO) / T34 (CENTRO) — P04 acceso + P06 orientación/recursos
- ISGC-P04-16 Tasa de adecuación del título (%)
- ISGC-P04-17 Tasa de ocupación del título (%)
- ISGC-P04-18 Tasa de preferencia del título (%)
- ISGC-P04-19 Tasa de renovación / nuevo ingreso (%)
- ISGC-P06-01 Satisfacción del alumnado con apoyo y orientación académica
- ISGC-P06-02 Satisfacción del alumnado con orientación profesional
- ISGC-P06-03 Satisfacción del alumnado con recursos materiales e infraestructuras
- ISGC-P06-04 Satisfacción del profesorado con recursos materiales e infraestructuras

### T35 (TÍTULO) / T36 (CENTRO) — P07 Satisfacción
Ruta: `P07 - Medición de Resultados/`
- ISGC-P07-01_01 Tasa de respuesta de la encuesta. Alumnado (%)
- ISGC-P07-01_02 Tasa de respuesta de la encuesta. PDI (%)
- ISGC-P07-02 Satisfacción global del alumnado con el título
- ISGC-P07-03 Satisfacción global del PDI con el título
- ISGC-P07-04 Satisfacción global del PAS con el Centro

### T37 (TÍTULO) / T38 (CENTRO) — P07 Egresados (POR AÑO DE EGRESO)
Ruta: `P07 - Medición de Resultados/` y `Encuestas Egresados/Encuesta de Egresados Detallado`
- ISGC-P07-01_03 Tasa de respuesta de la encuesta. Egresados (%)
- ISGC-P07-05 Tasa de inserción profesional (cualquier sector) (%)
- ISGC-P07-06 Tasa efectiva de inserción en sector relacionado (%)
- ISGC-P07-07 Tasa de autoempleo (%)
- ISGC-P07-08 Tasa de inserción con movilidad geográfica (%)
- ISGC-P07-09 Satisfacción de egresados con los estudios realizados
- ISGC-P07-10 Satisfacción de egresados con las competencias adquiridas
- NOTA: P07-05 a 10 = encuestas a egresados de 2–3 cursos antes.

### T39 — P07 BAU (Buzón de Atención al Usuario). TÍTULO (filas 1-4) y CENTRO (filas 7-10)
- ISGC-P07-11 Nº quejas/reclamaciones respecto a nº usuarios
- ISGC-P07-12 Nº incidencias docentes respecto a nº usuarios
- ISGC-P07-13 Nº sugerencias respecto a nº usuarios
- ISGC-P07-14 Nº felicitaciones respecto a nº usuarios

## Otras tablas con fuente LinceBI (no en Anexo 1)
- **Personal académico (Anexo 2 / T40)**: `P05 - Gest. Personal Docente/P05 - Personal
  docente disponible para impartir el título` (descargar informe ACCUA) y
  `P05-01 Evolución del personal académico del título`.
- **Calificaciones por asignatura (Anexo 4 / T44 y T21)**: `P04 - Gest. Procesos de
  Enseñanza-Aprendizaje/Porcentaje de Calificaciones por Asignatura y Plan`.

## Datos que no están en LinceBI

Son datos de gestión del centro; pídelos al usuario desde el principio (ver `SKILL.md`):
plazas del título doble, prácticas curriculares (créditos, plazas ofertadas, estudiantes
por curso, convenios con plazas y tutores, tutores académicos con dedicación), **créditos
reconocidos del curso** (criterio 3; LinceBI no publica ese informe), resultados de primer
curso si no se encuentran en LinceBI, y columnas de centro que ya no muestre LinceBI.

Si el autoinforme anterior cita la fuente de uno de estos datos (p. ej. la ruta de un
informe del Sistema de Información), reprodúcela en el `[PENDIENTE]` para que la
coordinación lo obtenga, y cita el valor del curso anterior solo como antecedente fechado.

## Esquema del JSON de datos (entrada del script de relleno)

```json
{
  "identificacion": {
    "Universidad": "Universidad de Cádiz",
    "ID Ministerio": "",
    "Denominación del título": "Grado en …",
    "Curso académico de implantación": "",
    "Web de la titulación": "",
    "Oferta de título doble": "NO",
    "En su caso, especificar la/las titulación/es y el/los centro/s": "",
    "En caso de ser un título conjunto, especificar las universidades donde se imparte": "",
    "Modalidad de enseñanza (presencial, semipresencial-híbrida, virtual, a distancia)": "Presencial",
    "En su caso, fecha de la última renovación de la acreditación": "",
    "En su caso, créditos prácticos obligatorios": "",
    "En su caso, estructuras curriculares específicas": ""
  },
  "encabezado": {
    "curso": "2024/25",
    "convocatoria": "2026",
    "titulo": "GRADO EN …",
    "centro": "Facultad de …"
  },
  "anios": ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"],
  "anios_egresados": ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24"],
  "extraccion": {"entorno": "data.uca.es", "fecha": "2026-03-01"},
  "indicadores": {
    "ISGC-P04-01": {"titulo": {"2020-21": "78,5", "2024-25": "81,2"}, "centro": {}},
    "ISGC-P04-09|Movilidad entrante internacional": {"titulo": {}, "centro": {}},
    "ISGC-P07-01_03": {"titulo": {"2023-24": "29,55% (13/44)"}, "centro": {}},
    "ISGC-P07-05": {"titulo": {"2023-24": "62,0"}, "centro": {}}
  },
  "puntos": {
    "1": {"fuertes": ["…"], "debiles": [{"punto": "…", "acciones": ["…"]}]},
    "6": {"fuertes": [], "debiles": []}
  },
  "plan_mejora": [
    {"origen": "Punto débil nº 1 …", "accion": "…", "evidencia": "…",
     "prioridad": "Alta", "responsable": "…", "inicio": "", "fin": "", "indicador": ""}
  ]
}
```

Claves de `indicadores`: el **código ISGC**; para P04-09 (movilidad) añade el sufijo
`|<subfila>` con el texto exacto de la subfila. Los valores son cadenas por año. Los
años que falten se dejan vacíos. `extraccion` registra el entorno de LinceBI y la fecha
de extracción (el script avisa si falta o si el entorno es `datapru`). El bloque `puntos`
se indexa por número de criterio (1–7). `plan_mejora` es una lista de filas.
