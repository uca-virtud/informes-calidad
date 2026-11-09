# Materiales del Servicio de Calidad (convocatoria 2027)

Documentos institucionales que el Servicio de Calidad de la UCA facilitó en noviembre de 2026
para la versión 8 de la skill. Son la fuente de la plantilla, las referencias y la rúbrica v3:
cuando cambien, se sustituye el fichero aquí y se actualiza lo que depende de él.

| Fichero o carpeta | Contenido | Dónde se usa |
|---|---|---|
| `plantilla-autoinforme-seguimiento-2027.docx` | Formato del autoinforme de seguimiento de 2027, común a la prueba piloto, al resto de títulos y a los que van a ACCUA. | Copia en `skills/uca-informes-calidad/assets/` |
| `guia-rapida-autoinformes.docx` | Guía rápida de apoyo (octubre de 2026) contra los errores recurrentes en la cumplimentación. | `references/guia-redaccion.md` (sección «Formato, enlaces y entrega» y checklist) y `scripts/depurar_instrucciones.py` (aviso de enlaces restringidos) |
| `recomendaciones-accua-mas-solicitadas.docx` | Recomendaciones de ACCUA más solicitadas en las renovaciones del año anterior; se exigen también en los seguimientos que van a ACCUA. | `references/recomendaciones-accua.md` |
| `recomendaciones-historicas/{grado,master}/` | Recomendaciones de ACCUA a los títulos de la UCA de 2022 a 2026, por tipo de título y criterio (C1-C7). | `references/recomendaciones-accua.md` (síntesis genérica, sin nombres de títulos) |
| `comparativas/{grado,master}/` | Indicadores de otras universidades (SIIU) para comparar (uso opcional). | `references/mapa-indicadores-lincebi.md` (sección «Comparativas»); los ficheros no van en el zip |

Solo en local (`.gitignore`), porque contienen datos personales:

- `revisiones/`: revisiones comentadas en Word de la rúbrica, de la skill y del borrador de
  Historia (E07), y las hojas originales de valoración de la ESI (E04-E06).
- `censos-ptgas/`: censos del PTGAS por campus, usados en el apartado 5.4. Pendiente de
  confirmar si LinceBI los publica.
