# Procedencia y verificaciones

Este paquete reúne el proyecto conceptual trabajado en Deswik CAD 2026.1, su ficha de datos y geometría auxiliar. Los originales se conservan en C:\Users\moise\Documents\Codex\2026-10-05\hol\outputs; se copiaron, no se movieron.

## Exportaciones de geometría

- Veta_75_ESE_solido_1_3m.dxf: sólido cerrado de potencia variable conceptual, con superficie central incluida. Es el exportado usado para la importación del modelo sólido.
- Veta_75_ESE_1000m.dxf: líneas guía de la construcción anterior, conservadas como referencia; no sustituye al sólido definitivo.
- La topografía original se conserva en el DUF; este paquete no añade otra copia DXF de esa topografía.

## Evidencias originales

Veta_solido_validacion_original.json registra las comprobaciones geométricas y la lectura Deswik al guardar el sólido anterior. Veta_atributos_verificacion_original.json registra la lectura nativa de los 16 atributos importados. Se preservan sin modificar: sus rutas y nombres de capa corresponden a la etapa anterior a organizar proyecto-deswik. No deben interpretarse como inventario final de capas.

El respaldo PMS_2026_VETA_CON_DATOS_EJEMPLO.duf contiene la versión guardada con atributos antes de esta organización. El DUF de la raíz es el principal para continuar.

El manifiesto de copias registra origen, tamaño y SHA-256; los archivos copiados se comprobaron contra sus originales. Los archivos de bloqueo .lck, registros del puente y componentes MCP no forman parte de los datos del proyecto.

## Organización del proyecto principal

El proyecto fue guardado como C:\Users\moise\OneDrive\Escritorio\proyecto-deswik\proyecto-deswik.duf. Las capas se agruparon como topografía, geología, referencias, superficies auxiliares y guías. Durante la reorganización, el handle del sólido cambió de 2503 / 9C7 a 2676 / A74; su GUID 1387534c-b5c9-4846-b6c5-8d2e859c9c84, volumen y número de vértices se conservaron.

La ficha CSV de 01_datos y su diccionario se actualizaron a HANDLE=A74. El manifiesto original documenta las copias iniciales previas a esta adaptación; el inventario final registra los archivos finales y sus hashes. Las verificaciones con sufijo _original siguen siendo evidencia histórica, con el handle y capas de la etapa anterior.
