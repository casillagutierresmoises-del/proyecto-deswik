# proyecto-deswik

Abrir **proyecto-deswik.duf** en Deswik CAD. Ese es el proyecto principal; conserva la topografía y la veta conceptual con sus atributos. El proyecto fue guardado desde la sesión Deswik con las capas organizadas.

## Organización

| Ubicación | Contenido |
|---|---|
| proyecto-deswik.duf | Proyecto principal de trabajo |
| 01_datos | Ficha CSV vigente y diccionario de los campos |
| 02_geometria | Exportaciones DXF del sólido y de las líneas guía |
| 03_documentacion | Ficha del modelo, procedencia y verificaciones |
| 04_respaldo | Copia del proyecto anterior a esta organización |
| Backup | Respaldos automáticos generados por Deswik al guardar |

La entidad del sólido se identifica con **VETA_ID=VETA_001**, GUID **1387534c-b5c9-4846-b6c5-8d2e859c9c84** y handle actual **2676 decimal / A74 hexadecimal**. La ficha CSV se relaciona con esa entidad mediante HANDLE. Los handles pueden cambiar al modificar capas o entidades: comprobar VETA_ID y GUID antes de volver a importar una ficha. La organización mantuvo el GUID y la geometría del sólido; el handle anterior era 2503 / 9C7.

## Capas del proyecto

| Grupo | Contenido |
|---|---|
| 01_TOPOGRAFIA | Topografía original; superficie en 01_SUPERFICIE |
| 02_GEOLOGIA_VETA_001 | 01_SOLIDO_POT_1_3M y 02_SUPERFICIE_CENTRAL |
| 03_REFERENCIAS | SOLIDOS y LAYPOL originales |
| 04_SUPERFICIES_AUX | Superficies auxiliares originales |
| 90_GUIAS_VETA | MODELO_GUIA_1000M |

El sólido de la veta está en **02_GEOLOGIA_VETA_001\01_SOLIDO_POT_1_3M**. La superficie central está separada y las líneas guía permanecen disponibles como referencia.

## Datos disponibles

La veta tiene buzamiento de 75°, dirección de buzamiento ESE (azimut 108.815301°), potencia verdadera conceptual de 1 a 3 m y extensión vertical de 1000 m. El volumen geométrico es 2537039.801976 m³.

**Au 4.2 g/t, Ag 65 g/t y densidad 2.7 t/m³ son ejemplos sintéticos, sin ensayes ni mediciones.** El tonelaje 6850007.465335 t resulta de multiplicar el volumen por esa densidad de ejemplo. No hay clasificación de recursos, reservas, interpolación de leyes ni modelo de bloques. La potencia variable también es una hipótesis geométrica.

El CSV usa coma como separador y punto decimal. Los 16 atributos nativos se importaron como texto; convertir explícitamente los campos numéricos antes de calcular. No reemplazar datos ausentes por cero.

Para continuar: abrir el DUF principal, consultar Veta_ficha.md y Diccionario_atributos.csv, y sustituir los ejemplos con información trazable cuando se disponga de muestreo real.

## Verificación del guardado

Se confirmó el proyecto guardado sin cambios pendientes, 22 capas y los 16 atributos del sólido coincidentes con la ficha CSV. La veta mantiene su GUID, volumen 2537039.8019757625 m³ y 5522 vértices. Los campos globales de atributos presentes en la topografía están vacíos; las leyes de ejemplo pertenecen al sólido de la veta.

La evidencia vigente está en [Verificacion_proyecto_deswik.json](03_documentacion/Verificacion_proyecto_deswik.json). Consultar [Inventario_capas.csv](03_documentacion/Inventario_capas.csv) para los nombres y estados nativos, y [Inventario_archivos_sha256.csv](03_documentacion/Inventario_archivos_sha256.csv) para tamaños y hashes del paquete final.

**proyecto-deswik.duf.lck es el archivo temporal de bloqueo de Deswik mientras el proyecto está abierto. No borrarlo ni moverlo durante la sesión.** Se excluye del inventario de datos. La carpeta Backup contiene los respaldos automáticos de Deswik; el respaldo manual anterior está separado en 04_respaldo.
