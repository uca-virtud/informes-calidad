# Rúbrica de evaluación de borradores

Versión: 3

Se puntúa un borrador generado por la skill frente a la **norma** (plantilla del Servicio de
Calidad del año de la convocatoria, guía de ACCUA/DEVA, guía rápida y recomendaciones de ACCUA
recopiladas por el Servicio de Calidad en [`docs/calidad-2026/`](../calidad-2026/README.md),
procedimientos del SGC de la UCA, memoria verificada) y a los **datos verificables**. El
autoinforme humano es una referencia, no la verdad absoluta: puede contener errores u omitir lo
que pide ACCUA, sobre todo en los títulos que ese año no van a ACCUA. Por eso el borrador cumple
la norma aunque el humano no lo haga, y el Servicio de Calidad valora también los borradores
para comprobar que siguen los requisitos de ACCUA. Cuando el borrador y el humano difieren,
primero se decide la causa (tabla de causas) y solo las diferencias de causa **S** restan puntos.

No se premia parecerse al humano en extensión ni en número de puntos fuertes o débiles: esas
cifras se miden (`evaluacion.py medir`), pero no se puntúan.

## Escala

| Nota | Significado |
|---|---|
| 2 | Correcto: la coordinación podría usarlo con retoques menores. |
| 1 | Aprovechable: hay que corregir o completar algo relevante. |
| 0 | No aprovechable: hay que rehacerlo o falta. |

## Dimensiones

| Dim. | Qué se evalúa | 2 | 1 | 0 |
|---|---|---|---|---|
| D1 | **Identificación del título** (tabla de identificación) | Todos los campos correctos según la memoria y el autoinforme anterior | 1–2 campos erróneos o `[PENDIENTE]` evitables | 3 o más campos erróneos |
| D2 | **Indicadores del Anexo I** (valores y cabeceras de cursos y cohortes) | ≥95 % de los valores comparables coinciden o difieren por causa D, I o H; cursos y cohortes bien alineados | 80–95 %, o una tabla con columnas desalineadas | <80 %, o varias tablas desalineadas |
| D3 | **Cobertura, evidencias y valoraciones** (todos los criterios y subcriterios de la plantilla del año, con las evidencias y valoraciones que pide ACCUA en cada uno) | Todos los subcriterios conservan su subdivisión y tienen análisis; están todas las evidencias y valoraciones que pide ACCUA; cada enlace a UCADrive lleva ruta, usuario y contraseña (o `[PENDIENTE]` para que los complete la coordinación); los `[PENDIENTE]` solo afectan a datos internos no aportados | Algún subcriterio vacío, fusionado o sin subdivisión; falta alguna evidencia o valoración que pide ACCUA; un enlace a UCADrive sin ruta, usuario ni contraseña; o un `[PENDIENTE]` evitable con LinceBI o con la entrada | Varios subcriterios vacíos o suprimidos, faltan varias evidencias o valoraciones, o falta un apartado obligatorio (p. ej. 6.3) |
| D4 | **Calidad del análisis** (no solo los indicadores: también procedimientos, coordinación, recursos y acciones realizadas; evolución, comparación con los objetivos de la memoria, causas) | Valora con evidencias lo que pide cada subcriterio, interpreta la evolución, compara con los objetivos de la tasa correcta y da causas plausibles y coherentes con los datos | Análisis descriptivo, limitado a los indicadores, sin causas o con alguna comparación incorrecta | Análisis ausente, contradictorio con los datos o genérico |
| D5 | **Puntos fuertes, puntos débiles y plan de mejora** | Puntos concretos y del curso en cada criterio; es punto débil toda satisfacción por debajo de 2,5 (escala 1-5), toda tendencia negativa durante dos cursos seguidos u otro hecho documentado que requiera mejora; el plan recoge todos los puntos débiles y todas las recomendaciones vivas de ACCUA; cada acción tiene un único responsable, evidencias y fechas (o `[PENDIENTE]` justificado) | Puntos genéricos, algún punto débil omitido o no asumible, o acciones sin enlazar, sin responsable o sin fechas | Faltan, o el plan de mejora no recoge los puntos débiles ni las recomendaciones |
| D6 | **Recomendaciones de ACCUA** (tabla del criterio 2 y plan de mejora) | Están todas las que ACCUA no ha cerrado, en la tabla del criterio 2 y en el plan de mejora, con numeración original y estado o acción | Falta alguna, se renumeran o solo aparecen en uno de los dos sitios | No se recogen o se inventan |
| D7 | **Formato, estilo y anexos** (plantilla del año, códigos `PF/PD/AM-<CENTRO>-crit.n`, sin instrucciones ni `XXXX`, registro formal, enlaces según la guía rápida, Anexos I a IV) | Documento limpio y fiel a la plantilla; los cuatro anexos (I indicadores, II personal académico, III prácticas externas, IV calificaciones) completos y con su formato; enlaces a evidencias públicas o en UCADrive, sin enlaces a sistemas de acceso restringido (LinceBI, GADES, ICARO, Campus Virtual) | Restos de instrucciones, códigos irregulares, estilo impropio en algún apartado, un anexo incompleto o con formato alterado, o algún enlace a un sistema restringido | Plantilla alterada, algún anexo vacío o ausente, o documento difícil de usar |

Si una dimensión no aplica al caso (p. ej. D6 sin informe de ACCUA), se anota `NA` y no cuenta en
la media.

## Bloqueantes

Se anotan aparte (sí/no) y se señalan en el resumen, con independencia de las notas:

- **B1** Dato inventado: un valor, nombre o hecho que no procede de la entrada, LinceBI ni la norma.
- **B2** Valor imposible o contradictorio: (a) fuera del rango que permite la definición del
  indicador (satisfacción >5, rendimiento, éxito, abandono, graduación o eficiencia >100 %);
  la ocupación, la preferencia y otros cocientes con denominador distinto pueden superar el
  100 % y no cuentan; o (b) el mismo indicador, ámbito (título o centro) y curso aparece con
  dos valores distintos dentro del borrador. Las comparaciones o valoraciones erróneas
  (p. ej. «supera al centro» cuando no lo hace) no son B2: se penalizan en D4. En casos muy
  raros, un indicador acotado supera el 100 % en LinceBI (p. ej. por créditos reconocidos o
  expedientes recalculados): si el borrador copia ese valor tal como sale en LinceBI, no es B2,
  pero queda pendiente de revisión experta.
- **B3** Datos de pruebas: extracción desde `datapru.uca.es` o sin entorno y fecha registrados.

## Causas de las discrepancias

| Causa | Significado | ¿Penaliza a la skill? |
|---|---|---|
| **S** | Skill: la instrucción falta, es ambigua o es incorrecta, o la IA no la siguió. | Sí |
| **D** | Datos de LinceBI: el valor cambió entre la extracción humana y la de la IA. Hay indicadores que varían según el momento del año o de un curso a otro por el cierre de expedientes; también influyen la fecha y la ventana de cursos. | No |
| **I** | Dato interno del centro no aportado en la entrada (prácticas, convenios, doble título…), o tabla que no sale de LinceBI por protección de datos: reconocimiento de créditos (3.3) y satisfacción con las asignaturas (6.4), que solo ve la coordinación en el UCADrive del Servicio de Calidad. | No, si quedó `[PENDIENTE]` |
| **H** | Error del humano: el borrador es correcto y el autoinforme humano no. | No; se anota como hallazgo |
| **E** | Editorial: misma información con distinta redacción u orden. | No |

Las causas **H** e **I** y los bloqueantes quedan siempre como «pendientes de revisión experta»
en la ficha.

## Cambios de versión

Si se modifica la rúbrica, sube el número de versión y vuelve a puntuar con el corrector B las
ejecuciones anteriores para que el historial siga siendo comparable. Excepción: si la versión
nueva exige una plantilla distinta de la que usaron las ejecuciones anteriores, no se vuelven a
puntuar, porque esos borradores no podían cumplirla; el historial indica la versión de cada
fila y las comparaciones se hacen solo entre ejecuciones con la misma versión.

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-10-02 | Versión inicial. |
| 2 | 2026-10-03 | B2 precisado: solo indicadores acotados por definición y contradicciones del mismo indicador, ámbito y curso; las comparaciones erróneas van a D4. |
| 3 | 2026-11-09 | Revisión del Servicio de Calidad y calibración con las valoraciones de la ESI: la norma incluye la plantilla del año, la guía rápida y las recomendaciones de ACCUA; D3 exige subdivisiones, evidencias, valoraciones y accesos a UCADrive; D4 no se limita a los indicadores; D5 fija los umbrales de punto débil e incluye las recomendaciones en el plan; D6 las exige en el criterio 2 y en el plan; D7 incluye los Anexos I a IV y los enlaces; B2 y causas D e I precisadas. Empieza en E10, con la plantilla de 2027; E01–E09 no se vuelven a puntuar. |
