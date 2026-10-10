# Piloto mecanizado: proyecto-deswik

Copia derivada del panel de 50 m de rumbo y 30 m de altura. Abrir `proyecto-deswik-mecanizado.duf`. Las 1407 entidades originales, la topografía, sus puntos y la veta se conservan. La revisión anterior está en `../05_PILOTO_CYR`.

La rampa tiene sección nominal 4,5 × 4,5 m, radio de eje 20 m y pendiente de 10%; las galerías y cortes, 3,5 × 3,5 m. Incluye accesos, estocadas, cruces, estación de carga y bocamina con bancada calculada contra los triángulos originales del terreno. Las dimensiones finales y comprobaciones están en `03_documentacion/Manifest_mecanizado.json`.

Flota de referencia: Sandvik LH307 con cucharón estándar bare-lip, TH315 y DD210 B14SNV/CFX-XS opcional. Las fichas y verificación de gálibos son referencias estáticas; falta comprobar barrido de vehículos, maniobras completas, sostenimiento, ventilación y salidas. Es geometría conceptual para desarrollar el proyecto.

Los diez cortes representan etapas sucesivas con relleno, no diez cavidades abiertas a la vez. Las bandas de mineral y guías se guardan apagadas para facilitar la vista; pueden activarse en Layer Control. El modelo Datamine de 14000 bloques permanece vinculado por ruta relativa y puede activarse en Geomodel Display. Au, Ag y densidad son ejemplos sintéticos sin ensayes; no se declaran recursos ni reservas.

`01_datos` contiene DM, CSV y TIN original; `02_geometria`, DXF auxiliares; `03_documentacion`, fuentes, atributos, manifiestos y comprobaciones. El archivo quedó abierto y guardado en Deswik, con la capa activa `03_PILOTO_MECANIZADO` y la primera fase visible. Se comprobaron seis muestras en la sesión y todas las geometrías exportadas después del guardado. Se conservó la distribución de ventanas. El estado final figura en `03_documentacion/Estado_mecanizado.json` y el informe en `03_documentacion/CAD_guardado_verificacion.json`. Los informes de lectura previos corresponden a la versión anterior al guardado en CAD; ambos hashes quedan identificados en el manifiesto.
