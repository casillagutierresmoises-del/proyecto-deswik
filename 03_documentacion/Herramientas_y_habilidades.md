# Herramientas preparadas para proyecto-deswik

Preparación y pruebas: 2026-10-05.

## Instalado

- **mineria-subterranea-deswik**: métodos de explotación, vocabulario ES/EN, orientación estructural, abreviaturas y contexto del proyecto. Incluye fuentes primarias; conserva las leyes y densidad actuales como ejemplos.
- **deswik-data-workflows**: inspección de CSV y mallas DXF, tratamiento de unidades, identificadores y procedencia. Tiene un inspector reutilizable de solo lectura.
- **jupyter-notebook**: habilidad oficial descargada de [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook) para análisis reproducibles.
- **deswik-fast-control**, mejorada: consultas nativas antes de mouse, recuperación de diálogos y lectura de atributos con límites. Conserva la distribución de ventanas preferida.

Las habilidades están en `C:/Users/moise/.codex/skills`. Entran en la selección de habilidades en el próximo turno; si alguna no aparece, reiniciar Codex. Sus scripts ya pueden ejecutarse por ruta absoluta.

## Entorno de datos

Python aislado: `C:/Users/moise/.codex/tools/mineria-deswik/.venv/Scripts/python.exe`.

| Biblioteca | Versión instalada | Uso |
|---|---|---|
| ezdxf | 1.4.4 | Capas, entidades y geometría DXF |
| numpy | 2.5.3 | Coordenadas y cálculos vectorizados |
| pandas | 3.0.6 | CSV y tablas tipadas |
| scipy | 1.18.1 | Cálculos numéricos y consultas espaciales |
| pyarrow | 25.0.1 | Parquet para tablas de mayor tamaño |
| trimesh | 5.1.1 | Cierre, orientación y volumen de mallas |

Instalación por ruedas binarias de PyPI, sin extras. `requirements-lock.txt` guarda versiones y `pip-check.txt` confirmó dependencias compatibles en esa carpeta. Las herramientas no necesitan alterar el Python de Deswik.

## Puente Deswik

El MCP registrado **deswik-local-readonly** usa ahora la copia persistente `C:/Users/moise/.codex/tools/mineria-deswik/deswik_mcp.py`, versión **0.3.0**, con **9 herramientas**. Se añadieron atributos por capa y una revisión conjunta de documento, entidades y atributos. El puente nativo TCP 9595 ya existente permanece como conexión con Deswik; no se instaló otro add-in.

El nuevo proceso se probó por stdio usando el comando/ruta registrados. La sesión actual puede conservar la lista anterior: **reiniciar Codex carga las herramientas nuevas; Deswik puede permanecer abierto**. Los scripts de inspección ya funcionan por ruta absoluta. Configuración anterior respaldada en la carpeta de herramientas. Configuración ajena a este MCP preservada y validada como TOML.

La búsqueda del catálogo no devolvió un plugin específico Deswik/minería. GitHub, Computer Use y las habilidades de hojas/documentos existentes ya cubren sus funciones. Repositorios alternativos se revisaron como referencias; no se instalaron agentes que requieren otro CAD o una segunda conexión. [Puente comunitario original](https://github.com/botaoshen/deswik-mcp-plugin).

## Pruebas

- Cuatro habilidades pasaron el validador; la habilidad minera pasó una revisión independiente de selección de método y ambigüedad SLS.
- MCP: nueve herramientas declaradas, seis entradas inválidas rechazadas, capa de veta resuelta al handle actual y 16 atributos comprobados. Consulta conjunta medida: 93.421 ms en una prueba. Es latencia local del conector, no velocidad total ni mejora porcentual del asistente.
- Archivos reales: CSV de 1 fila y 16 campos completos; DXF del sólido con 5522 vértices y 11040 caras cerrado y orientado. Superficie central abierta correctamente diferenciada. Volumen, buzamiento 75°, azimut 108.815301° y potencia 1–3 m coherentes con la ficha.
- `proyecto-deswik.duf` conservó SHA-256 `9dad3c8ba2cb7c164bdf522c5616544080a45aa649ccc0f2d412a4d15a47f54d`. No se editaron geometrías ni se movieron ventanas en esta preparación.

Detalle estructurado: [Herramientas_verificacion.json](Herramientas_verificacion.json). Las evidencias de prueba están en `C:/Users/moise/Documents/Codex/2026-10-05/hol/work/tooling-review`.

## Fuentes y límites prácticos

Las habilidades y puentes aportan procedimientos y acceso a datos; no modifican el modelo de IA ni habilitan visión continua de toda la pantalla. Se consulta el estado y se toman capturas al trabajar. La rapidez depende también de la operación CAD y de las decisiones necesarias.

Fuentes para el contexto minero: [Penn State](https://courses.ems.psu.edu/mng230/node/899), [ANM, glosario](https://www.anm.gov.co/sites/default/files/DocumentosAnm/glosariominero.pdf), [CIM, prácticas de datos](https://mrmr.cim.org/media/1146/cim-mrmr-bp-guidelines_2019_may2022.pdf) y [Deswik SO](https://www.deswik.com/products/so). Las referencias completas están dentro de la habilidad minera. Un producto publicado no confirma que su módulo esté licenciado en este PC.

Formatos y software: [ezdxf POLYFACE](https://ezdxf.readthedocs.io/en/stable/tutorials/polyface.html), [trimesh](https://trimesh.org/trimesh.html), [pandas](https://pandas.pydata.org/docs/user_guide/io.html), [Arrow](https://arrow.apache.org/docs/python/), [OpenAI MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) y [OpenAI habilidades](https://learn.chatgpt.com/docs/build-skills).

El DXF R12 auxiliar no declara unidad con INSUNITS; los metros proceden del diccionario/procedencia del proyecto. El inspector no prueba autointersecciones, estabilidad ni validez geológica. Au/Ag/densidad y tonelaje continúan identificados como ejemplos; la selección de un método requiere los datos pertinentes del proyecto.
