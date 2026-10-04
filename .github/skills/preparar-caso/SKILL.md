---
name: preparar-caso
description: >-
  Prepara un caso nuevo de evaluación de la skill de autoinformes a partir del nombre de
  un título de la Universidad de Cádiz: localiza en la web de su facultad o escuela el
  autoinforme presentado y los documentos de entrada (memoria, autoinforme anterior,
  informe ACCUA/DEVA, plan de mejora), da de alta la fila en docs/evaluacion/casos.csv y
  los descarga en evals/casos/<id>/entrada/ y referencia/. Úsala cuando el usuario pida
  «preparar», «dar de alta» o «añadir» un caso o un título para evaluar.
---

# Preparar un caso de evaluación

Entrada: el nombre de un título de la UCA (p. ej. «Grado en Historia»). Salida: el caso dado
de alta en `docs/evaluacion/casos.csv`, con sus documentos en `evals/casos/<id>/` y su
procedencia en `fuentes.md`, listo para `evaluacion.py nueva <id>` (ver
[`docs/evaluacion/procedimiento.md`](../../../docs/evaluacion/procedimiento.md)).

El alta y la descarga las hace el script `tools/evaluacion/evaluacion.py`; tu trabajo es
**encontrar y elegir** los documentos con criterio, porque cada centro publica de forma
distinta.

## 1. Localizar las páginas del título

1. Busca el título en `https://www.uca.es/grados/` (o en el listado de másteres): enlaza a
   la página del título en la web del centro. Si no aparece, parte de
   `https://www.uca.es/centros/`.
2. Consulta [`references/centros.md`](references/centros.md): si el centro ya está
   descrito, ve directo a sus páginas; si no, recorre la página del título y sus
   subpáginas de calidad, informes y datos generales.
3. Lista los enlaces de cada página con el subcomando `enlaces`, que también muestra los
   que están dentro de desplegables:

   ```bash
   python3 tools/evaluacion/evaluacion.py enlaces <url-de-la-página>
   ```

   Cada línea es `DOC|PÁG | texto del enlace | URL`. `--todos` quita el filtro. Anota,
   para cada documento, el texto del enlace, la URL y la página donde aparece.

## 2. Fijar el caso

- **Referencia** (`autoinforme-humano`): el autoinforme del **último curso publicado** del
  título. Descárgalo a un directorio temporal, lee la portada con `pypdf` y anota el tipo
  (`seguimiento` o `renovación`), el curso (`AAAA-AA`) y la convocatoria (`AAAA`).
- **Entrada**: solo documentos que la coordinación tenía antes de redactar la referencia;
  nada posterior, o el caso deja de medir la skill:

  | Rol | Documento | Obligatorio |
  |---|---|---|
  | `memoria` | Memoria vigente durante el curso del caso (la verificada o su última modificación anterior al autoinforme) | Sí, en seguimiento |
  | `autoinforme-anterior` | Autoinforme del curso anterior al de referencia | Sí, en seguimiento |
  | `informe-accua` | Último informe de la agencia (ACCUA/DEVA: seguimiento, modificación o renovación) **anterior** al autoinforme de referencia | Si existe |
  | `plan-mejora` | Plan de mejora del curso anterior (el del curso del caso acompaña a la referencia: no lo uses) | Si existe |

  Fíjate en la fecha de la ruta (`/wp-content/uploads/AAAA/MM/`) y en el año del nombre del
  fichero: si la única memoria publicada es posterior al autoinforme de referencia,
  señálalo al usuario.
- **Id**: `<SIGLAS>-<seg|ren>-<AAAA>`, con las siglas del título y el curso en cuatro cifras
  (`2024-25` → `2425`), como los casos existentes. Comprueba que no esté ya en `casos.csv`.
- **Nivel**: `grado` o `máster`. **Centro**: siglas del centro, coherentes con las filas
  existentes.
- **seguimiento_accua**: `sí` o `no` solo si el autoinforme o el informe de la agencia lo
  dicen claramente; si no, déjalo vacío.

## 3. Confirmar con el usuario

Antes de descargar, usa `ask_user`, una pregunta cada vez:

- Si un rol tiene varios candidatos (versiones, memoria original y modificada) o falta un
  documento obligatorio, muestra los candidatos (texto del enlace, URL, fecha) y pregunta
  cuál usar. No elijas por tu cuenta.
- Pregunta **siempre** el `conjunto`: `aprendizaje` o `reserva` (nunca `excluido`).
- Muestra la selección final (id, tipo, curso, convocatoria y un documento por rol) y
  espera su conformidad.

## 4. Dar de alta y descargar

Escribe el manifiesto `evals/casos/<id>/fuentes.json` y ejecuta desde la raíz:

```bash
python3 tools/evaluacion/evaluacion.py caso evals/casos/<id>/fuentes.json
```

Formato del manifiesto (los campos son las columnas de `casos.csv` más `documentos` y
`notas`, opcional):

```json
{
  "id": "<SIGLAS>-seg-2425",
  "titulo": "Grado en …",
  "nivel": "grado",
  "centro": "<SIGLAS DEL CENTRO>",
  "tipo": "seguimiento",
  "curso": "2024-25",
  "convocatoria": "2026",
  "seguimiento_accua": "",
  "conjunto": "aprendizaje",
  "notas": "Decisiones tomadas y su motivo.",
  "documentos": [
    {"rol": "autoinforme-humano", "url": "https://….pdf", "pagina": "https://… (página donde está el enlace)"},
    {"rol": "autoinforme-anterior", "url": "https://….pdf", "pagina": "https://…"},
    {"rol": "memoria", "url": "https://….pdf", "pagina": "https://…"}
  ]
}
```

El script valida el manifiesto y descarga solo por `https` desde `uca.es` o
`juntadeandalucia.es`. Comprueba que cada fichero es PDF o DOCX y lo guarda con el nombre
del rol, sin sobrescribir nada. Después escribe `fuentes.md` (URL, página, fecha, tamaño,
SHA-256), confirma que el caso está completo y, solo entonces, añade la fila a
`casos.csv`.

- Si falla, no se añade la fila: corrige el manifiesto y repite (borra antes los ficheros
  ya descargados del caso si el error fue posterior a la descarga).
- Si una URL apunta a una página HTML, busca en ella el enlace directo al fichero.
- Si el usuario aporta a mano algún documento, cópialo con el nombre del rol y ejecuta con
  `--sin-descarga`.
- Comunica al usuario los `AVISO` (PDF escaneado o ilegible).

## Reglas

- De `referencia/` lee solo la portada: el caso es para evaluar, no para aprender de él.
- No copies nada de estos documentos a la skill del producto ni a la web (ver `AGENTS.md`).
- Si descubres cómo publica un centro aún no descrito, **propón** añadirlo a
  `references/centros.md`: páginas, nombres de los apartados y particularidades, sin datos
  de los autoinformes.
