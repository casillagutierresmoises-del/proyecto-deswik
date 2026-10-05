# Ficha de la veta VETA_001

## Identificación

- Proyecto principal: ../proyecto-deswik.duf, guardado en C:\Users\moise\OneDrive\Escritorio\proyecto-deswik.
- Entidad nativa: sólido Polyface, handle actual 2676 decimal / A74 hexadecimal.
- GUID del sólido: 1387534c-b5c9-4846-b6c5-8d2e859c9c84.
- Capa del sólido: 02_GEOLOGIA_VETA_001\01_SOLIDO_POT_1_3M.
- Superficie central: 02_GEOLOGIA_VETA_001\02_SUPERFICIE_CENTRAL.
- Guías: 90_GUIAS_VETA\MODELO_GUIA_1000M.
- Topografía: 01_TOPOGRAFIA\01_SUPERFICIE; hojas restantes originales conservadas.
- Revisión de datos: 2026-10-05_v1.
- Estado: SINTETICO_NO_ENSAYADO; origen de leyes: EJEMPLO_SIN_MUESTREO; clasificación: NO_CLASIFICADO.
- Atributos: 16 campos enlazados al sólido, verificables en la lectura nativa registrada. Todos se almacenaron como texto.

El handle anterior era 2503 / 9C7. Al organizar las capas pasó a 2676 / A74, conservando el GUID y la geometría. HANDLE es una clave de importación ligada a la entidad actual, no un identificador estable del proyecto. Conservar VETA_ID y GUID como referencias de identificación y confirmar el handle vigente antes de importar cambios.

## Geometría

| Parámetro | Valor | Unidad |
|---|---:|---|
| Buzamiento | 75 | grados |
| Azimut de buzamiento | 108.815301 | grados desde norte |
| Potencia verdadera mínima | 1 | m |
| Potencia verdadera máxima | 3 | m |
| Extensión vertical | 1000 | m |
| Volumen geométrico | 2537039.801976 | m³ |

La superficie central sigue un plano de 75° hacia ESE e intersecta la topografía. La profundidad se mide verticalmente bajo la traza superior, no como longitud sobre el plano. La potencia se mide perpendicularmente al plano y varía suavemente según una función conceptual; no procede de mediciones geológicas.

El sólido tiene 5522 vértices y 11040 triángulos. Antes de importarlo se comprobó cierre, orientación consistente y un solo componente conectado. El volumen calculado por Deswik coincide con el cálculo independiente con diferencia relativa inferior a 1e-9.

El cierre superior sigue la intersección central con la topografía. Los contactos laterales se desplazan perpendicularmente al plano y no se recortaron individualmente contra el terreno.

## Datos de ejemplo

| Campo | Valor | Unidad / procedencia |
|---|---:|---|
| AU_G_T_EJEMPLO | 4.2 | g/t, sintético |
| AG_G_T_EJEMPLO | 65 | g/t, sintético |
| DENSIDAD_T_M3_EJEMPLO | 2.7 | t/m³, supuesto |
| TONELAJE_T_EJEMPLO | 6850007.465335 | t, volumen × densidad de ejemplo |

Las leyes son constantes ilustrativas para todo el sólido. No hay muestreo, interpolación espacial, modelo de bloques ni estimación de recursos. El tonelaje describe una geometría hipotética con densidad supuesta; no representa mineral económicamente explotable.

## Continuación del proyecto

Relacionar futuras muestras por VETA_ID y coordenadas XYZ, conservando código de muestra, laboratorio, método, fecha, intervalo, resultados y QA/QC. Usar densidad medida, definir dominios geológicos y conservar los datos originales antes de distribuir leyes. Los valores sin información deben permanecer sin dato.

La ficha editable está en ../01_datos/Veta_atributos_ejemplo.csv. El diccionario explica unidades, significado y procedencia de cada campo.

## Comprobación final del proyecto organizado

La lectura nativa final confirmó el DUF guardado sin cambios pendientes; los 16 campos de la veta coinciden exactamente con la ficha CSV vigente, incluido HANDLE=A74. Se conservaron el GUID del sólido, el volumen 2537039.8019757625 m³, los 5522 vértices y las dos entidades seleccionadas. No hay leyes de ejemplo asignadas a la topografía.

Evidencia: [Verificacion_proyecto_deswik.json](Verificacion_proyecto_deswik.json). El [inventario de capas](Inventario_capas.csv) recoge las 22 capas nativas, incluidas las capas internas de Deswik conservadas. Los estados de visibilidad se registran tal como los devuelve Deswik y no describen otra vista del proyecto.

Los documentos con sufijo _original conservan la evidencia histórica anterior; usar la verificación del proyecto organizado para los handles y las capas actuales.
