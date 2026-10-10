# Comprobación dimensional de perfiles de referencia

El auditor `auditar_galibos.py` lee `equipos_referencia.json` y escribe `Verificacion_galibos_referencia.json`. No modifica geometría ni usa CAD. Evalúa rectángulos verticales centrados sobre un piso local contra la bóveda analítica `z(x)=pared+alza*sqrt(1-(2x/ancho)^2)`. La comprobación 2D es geométrica; no acredita maniobra, tránsito ni seguridad.

| Equipo de referencia | Principal 4.5×4.5, pared 3/alza 1.5: holgura lateral por lado / vertical mínima, m | Galería 3.5×3.5, pared 3/alza 0.5: holgura lateral por lado / vertical mínima, m |
|---|---|---|
| LH307 bare lip, 2.232×2.252 m | 1.134 / 2.050 | 0.634 / 1.133 |
| TH315 estándar, 2.274×2.395 m | 1.113 / 1.899 | 0.613 / 0.985 |
| DD210 CFX-XS, 1.400×2.735 m (FOPS alto conservador) | 1.550 / 1.691 | 1.050 / 0.723 |

Las cifras corresponden a una sección ideal sin sostenimiento ni servicios, con vehículo centrado y nivelado. La holgura vertical se toma en los bordes superiores del rectángulo, donde el techo es más bajo; no se usa solo la altura al eje.

En la cámara propuesta **6.5 m de ancho, pared 3.5 m, alza 1.7 m, altura al eje 5.2 m**, el rectángulo sustituto de ancho 2.232 m y altura H6=4.709 m tiene techo mínimo 5.096631 m sobre sus bordes; diferencia vertical 0.387631 m. Añadiendo únicamente para sensibilidad 0.25 m por lado y 0.25 m arriba, queda 0.083549 m. Esos 0.25 m no son un margen obligatorio ni validado.

Con altura sustituta 4.885 m y el mismo ejemplo de 0.25 m, la diferencia pasa a **−0.092451 m**. Es una banda de sensibilidad, no una combinación real de equipo seleccionada. Cambiar cucharón/cabina exige releer su columna exacta y recalcular. El informe incluye alturas de cámara 5.2/5.5 m, alturas sustitutas 4.709/4.885 m, desplazamientos de centro 0–1.25 m y bandas de ampliación lateral 0/0.15/0.25 m.

El ancho del portador se usa como sustituto conservador para este cálculo; **no es la envolvente real del cucharón articulado**, ni comprueba su trayectoria dentro de la caja del camión. Deben verificarse el arco completo de movimiento y la altura disponible fuera del eje.

El contrato estático del generador usa 16 divisiones del arco, por ángulos equidistantes, y perfiles verticales en gravedad. El auditor también calcula esa bóveda de cuerdas: en la cámara propuesta, H=4.709 m deja 0.381861 m sin ampliación y 0.077407 m con el ejemplo de 0.25 m; la banda H=4.885 m con ese ejemplo deja −0.098593 m. Estas cifras todavía requieren confirmar los parámetros contra la geometría final, no solo contra el código.

Pendiente confirmar que la geometría final use exactamente estos parámetros. Tampoco se evaluaron giro, inclinación longitudinal/lateral, voladizos, deformación de neumáticos, servicios ni espesor de soporte. Conservar estado conceptual.
