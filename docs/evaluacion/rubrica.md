# Rúbrica de evaluación de borradores

Versión: 2

Se puntúa un borrador generado por la skill frente a la **norma** (plantilla oficial, guía de
ACCUA/DEVA, procedimientos del SGC de la UCA, memoria verificada) y a los **datos verificables**.
El autoinforme humano es la referencia principal, pero no la verdad absoluta: puede contener
errores. Cuando el borrador y el humano difieren, primero se decide la causa (tabla de causas) y
solo las diferencias de causa **S** restan puntos.

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
| D3 | **Cobertura de apartados** (criterios y subcriterios con contenido) | Todos los subcriterios tienen análisis; los `[PENDIENTE]` solo afectan a datos internos no aportados | Algún subcriterio vacío o un `[PENDIENTE]` evitable con LinceBI o con la entrada | Varios subcriterios vacíos o falta un apartado obligatorio (p. ej. 6.3) |
| D4 | **Calidad del análisis** (interpretación de indicadores, evolución, comparación con los objetivos de la memoria, causas) | Interpreta la evolución, compara con los objetivos de la tasa correcta y da causas plausibles y coherentes con los datos | Análisis descriptivo, sin causas o con alguna comparación incorrecta | Análisis ausente, contradictorio con los datos o genérico |
| D5 | **Puntos fuertes, puntos débiles y plan de mejora** | Puntos concretos y del curso; cada punto débil es asumible por la coordinación y tiene acción con responsable y plazo (o `[PENDIENTE]` justificado) | Puntos genéricos, débiles no asumibles o acciones sin enlazar | Faltan, o el plan de mejora no recoge los puntos débiles |
| D6 | **Recomendaciones de ACCUA** (criterio 2 y plan de mejora) | Están todas las vivas, con numeración original y estado o acción | Falta alguna o se renumeran | No se recogen o se inventan |
| D7 | **Formato y estilo** (plantilla, códigos `PF/PD/AM-<CENTRO>-crit.n`, sin instrucciones ni `XXXX`, registro formal) | Documento limpio y fiel a la plantilla | Restos de instrucciones, códigos irregulares o estilo impropio en algún apartado | Plantilla alterada o documento difícil de usar |

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
  (p. ej. «supera al centro» cuando no lo hace) no son B2: se penalizan en D4.
- **B3** Datos de pruebas: extracción desde `datapru.uca.es` o sin entorno y fecha registrados.

## Causas de las discrepancias

| Causa | Significado | ¿Penaliza a la skill? |
|---|---|---|
| **S** | Skill: la instrucción falta, es ambigua o es incorrecta, o la IA no la siguió. | Sí |
| **D** | Datos de LinceBI: el valor cambió entre la extracción humana y la de la IA (volatilidad, fecha, ventana de cursos). | No |
| **I** | Dato interno del centro no aportado en la entrada (prácticas, convenios, doble título…). | No, si quedó `[PENDIENTE]` |
| **H** | Error del humano: el borrador es correcto y el autoinforme humano no. | No; se anota como hallazgo |
| **E** | Editorial: misma información con distinta redacción u orden. | No |

Las causas **H** e **I** y los bloqueantes quedan siempre como «pendientes de revisión experta»
en la ficha.

## Cambios de versión

Si se modifica la rúbrica, sube el número de versión y vuelve a puntuar con el corrector B las
ejecuciones anteriores para que el historial siga siendo comparable.

| Versión | Fecha | Cambio |
|---|---|---|
| 1 | 2026-10-02 | Versión inicial. |
| 2 | 2026-10-03 | B2 precisado: solo indicadores acotados por definición y contradicciones del mismo indicador, ámbito y curso; las comparaciones erróneas van a D4. |
