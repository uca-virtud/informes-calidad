# Procedimiento de evaluación de la skill

Cómo evaluar `skills/uca-informes-calidad` de forma sistemática. Cada **ejecución** evalúa
**un título** y se orquesta entera desde GitHub Copilot CLI: el agente principal
(orquestador) lanza dos subagentes y ejecuta el script `tools/evaluacion/evaluacion.py`.
El responsable del proyecto solo aporta los documentos y decide qué lecciones se aplican.

Piezas:

| Pieza | Qué es |
|---|---|
| `docs/evaluacion/casos.csv` | Catálogo de casos (título, tipo, curso, convocatoria, ACCUA, conjunto: `aprendizaje`, `reserva` o `excluido`). |
| `docs/evaluacion/rubrica.md` | Rúbrica cerrada: D1–D7 (0-1-2), bloqueantes B1–B3, causas S/D/I/H/E. |
| `docs/evaluacion/plantilla-cotejo.md` | Formato obligatorio de `cotejo-A.md` y `cotejo-B.md`. |
| `docs/evaluacion/plantilla-ficha.md` | Ficha de cada ejecución (la crea el script). |
| `evals/casos/<id>/entrada/` | Lo que recibiría la skill: autoinforme anterior, memoria, informe ACCUA… |
| `evals/casos/<id>/referencia/autoinforme-humano.*` | Autoinforme presentado por la coordinación. **Nunca** lo ve A al generar. |
| `evals/ejecuciones/Enn-<id>/` | Ficha, borrador, cotejos y métricas de la ejecución. |
| `evals/historial.md` | Tabla con todas las ejecuciones (la regenera `medir`). |

`evals/` contiene datos personales y no se versiona: al repositorio y a la web solo llegan
cifras agregadas y lecciones generalizadas.

## Requisitos previos (una vez)

1. MCP de LinceBI configurado en Copilot CLI contra `data.uca.es` (lo configura el
   responsable; el agente no ve las credenciales).
2. Entorno Python con `pip install -r tools/evaluacion/requirements.txt`.
3. Modelos fijos: **A** = `claude-opus-5.5` (genera y se autocoteja); **B** = `gpt-6.1-sol`
   (segundo corrector, de otra familia). Si cambian, se anota en la ficha y en el historial.
4. Que Copilot use la skill del repositorio (`skills/uca-informes-calidad/SKILL.md`), no una
   copia global antigua.

## Antes de la ejecución: el caso

1. Añade una fila a `casos.csv` (o reutiliza la existente). Elige el título **por
   variedad** (otro centro, máster, renovación…) frente a los ya evaluados.
2. Copia los documentos en `evals/casos/<id>/entrada/` (`autoinforme-anterior.*`,
   `memoria.*`, opcionalmente `informe-accua.*` y `plan-mejora.*`) y el autoinforme humano
   en `evals/casos/<id>/referencia/autoinforme-humano.*`.

## Pasos de una ejecución

Pídeselo al orquestador con: «Evalúa la skill con el caso `<id>` siguiendo
docs/evaluacion/procedimiento.md».

| Paso | Quién | Acción | Produce |
|---|---|---|---|
| 1 | Orquestador | `python tools/evaluacion/evaluacion.py nueva <id>` | `Enn-<id>/ficha.md` |
| 2 | Subagente A (`general-purpose`, `claude-opus-5.5`, segundo plano) | Prompt de generación | `borrador.docx`, `datos.json`, sección «Generación» de la ficha |
| 3 | Mismo subagente A (`write_agent`) | Prompt de autocotejo | `cotejo-A.md` |
| 4 | Subagente B (`general-purpose`, `gpt-6.1-sol`) | Prompt de segundo corrector | `cotejo-B.md` |
| 5 | Orquestador | `python tools/evaluacion/evaluacion.py medir Enn` | `metricas.json`, ficha completada, `evals/historial.md` |
| 6 | Orquestador → responsable | Resumen: notas, bloqueantes, pendiente de revisión experta y lecciones candidatas | Decisión en la ficha |

Reglas del orquestador:

- A no recibe la ruta de `referencia/` hasta el paso 3. B no recibe `cotejo-A.md`.
- Si A detecta `datapru.uca.es` o LinceBI no responde, se detiene la ejecución (bloqueante
  B3) y se avisa al responsable; no se continúa con datos de pruebas.
- El orquestador **no modifica la skill**. Las lecciones se aplican después, solo las que
  apruebe el responsable, en un cambio pequeño y con su propia versión.

## Prompts

Sustituye `<…>` con los datos de la ficha y de `casos.csv`.

### Paso 2: generación (A)

```text
Eres el subagente generador de una evaluación de la skill. Trabaja en la raíz del
repositorio uca-informes-calidad. Lee y sigue skills/uca-informes-calidad/SKILL.md (no uses
ninguna otra skill de autoinformes instalada) para redactar el autoinforme de <tipo> del
<titulo>, curso <curso>, convocatoria <convocatoria>.

No puedes preguntar al usuario. Estas son sus respuestas a lo que la skill pregunta:
- Tipo: <tipo>. ¿Seguimiento ACCUA?: <sí/no/no consta: asume sí y anótalo>.
- Indicadores: LinceBI (data.uca.es) mediante las herramientas lincebi_*.
- Documentos aportados: los de evals/casos/<id>/entrada/ (lístalos).
- Datos internos del centro: no se aportan; déjalos [PENDIENTE] como indica la skill.
Si la skill pidiera algo más, toma el supuesto más razonable y anótalo.

Prohibido: leer evals/casos/<id>/referencia/ y otras carpetas de evals/ejecuciones/;
modificar ficheros de skills/. Si el host de LinceBI no es data.uca.es,
detente y explícalo.

Escribe en evals/ejecuciones/<Enn-id>/: borrador.docx (entregable de la skill) y
datos.json (el JSON de datos con el bloque extraccion). Completa la sección
«Generación» de ficha.md (host, fecha de extracción, documentos usados, supuestos,
decisiones, incidencias). Termina con un resumen breve; no hagas todavía ningún cotejo.
```

### Paso 3: autocotejo (A)

```text
Ahora coteja tu borrador con el autoinforme presentado por la coordinación:
evals/casos/<id>/referencia/autoinforme-humano.*. No modifiques el borrador.

Puntúa con docs/evaluacion/rubrica.md y escribe evals/ejecuciones/<Enn-id>/cotejo-A.md
con el formato exacto de docs/evaluacion/plantilla-cotejo.md (no cambies los títulos de
sección ni las columnas de las tablas). Para cada discrepancia relevante asigna una causa
S/D/I/H/E; el autoinforme humano no es la verdad: si el borrador es correcto, la causa es
H. Propón lecciones solo para causas S: reglas generales sin datos del título, indicando
su respaldo (norma, otros títulos o «ninguno aún»). No edites la skill.
```

### Paso 4: segundo corrector (B)

```text
Eres un corrector independiente. Evalúa un borrador de autoinforme de calidad de la
Universidad de Cádiz generado por IA, comparándolo con el que presentó la coordinación.

- Borrador: evals/ejecuciones/<Enn-id>/borrador.docx (y datos.json si existe).
- Autoinforme humano: evals/casos/<id>/referencia/autoinforme-humano.*.
- Documentos de entrada que tuvo la IA: evals/casos/<id>/entrada/.
- Contexto de la generación: sección «Generación» de evals/ejecuciones/<Enn-id>/ficha.md.
- Reglas que debía seguir: skills/uca-informes-calidad/ (para decidir si una
  discrepancia es de causa S).

No leas cotejo-A.md ni otras ejecuciones. No modifiques nada salvo el fichero de salida.
Puntúa con docs/evaluacion/rubrica.md y escribe evals/ejecuciones/<Enn-id>/cotejo-B.md con
el formato exacto de docs/evaluacion/plantilla-cotejo.md. Justifica cada nota con una
evidencia concreta (apartado y texto o valor). El autoinforme humano no es la verdad: si
el borrador es correcto y el humano no, la causa es H.
```

### Línea base y cambios de rúbrica

Para ejecuciones anteriores al protocolo (E01–E03) o cuando cambia la versión de la
rúbrica, solo se lanza B (paso 4) sobre el borrador existente y después `medir`.

## Consolidación y decisiones

- `medir` toma como nota final la de B (o la de A si no hay B). Si A y B difieren en 2
  puntos o hay bloqueantes, H o I, la dimensión pasa a «pendiente de revisión experta».
- El responsable anota en la ficha qué lecciones aprueba, rechaza o deja como candidatas.
- Las métricas automáticas (extensión, PF/PD/AM, `[PENDIENTE]`, Anexo I) son aproximadas:
  el Anexo I cuenta los valores del borrador que aparecen en cualquier parte del texto
  humano, así que es solo una cota superior (en la línea base dio 97 % donde B comprobó
  menos del 80 % celda a celda). La nota de D2 la pone B comparando por celda.
- `medir` avisa de **huellas**: frases de 8 palabras que solo aparecen en la referencia de
  un título y también en la skill. Indican que la skill contiene texto de un caso de
  evaluación, lo que infla sus notas en ese caso.

## Reglas contra el sobreajuste

1. Cada título nuevo contrasta las lecciones anteriores: una lección solo pasa a
   **validada** cuando mejora (o no empeora) un título distinto evaluado después.
2. Filtro de admisión: la lección procede de la normativa o la guía, se observó en 2 o más
   títulos de 2 o más coordinaciones, o la aprueba la Unidad de Calidad. Si no, queda como
   **candidata**.
3. La skill no contiene datos, frases ni nombres de los casos de evaluación. Sus ejemplos
   literales proceden solo de títulos marcados como `conjunto = excluido` en `casos.csv`
   (hoy, GIM, cuyos autoinformes están en `samples/`), que nunca se evalúan. El aviso de
   huellas de `medir` lo comprueba; una frase suelta compartida con un título excluido del
   mismo centro es redacción común y puede quedarse.
4. El autoinforme humano es una referencia, no la verdad.
5. Elige el siguiente título por variedad; reserva algunos (`conjunto = reserva`) que no
   se usan para aprender y se evalúan en los hitos para detectar regresiones.
6. Cambios en la skill pequeños, versionados y aprobados por el responsable.

Estados de una lección: candidata → incorporada → validada en Enn (o insuficiente).
