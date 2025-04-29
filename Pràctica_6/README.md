# Pràctica 5: Moviment circular amb Python i Blender

## Fórmules de referència

Atenció! Com que treballem en tres dimensions, recorda que l'eix associat amb l'alçada és l'eix `Z`.

### MCU - Moviment Circular Uniforme

Velocitat angular constant:

$$
\omega = ct
$$

Angle:

$$
\varphi(t) = \varphi _0 + \omega t
$$

Posició eix X i eix Y (on r és el radi de la circumferència que descriu la posició de l'objecte):

$$
x(\varphi) = r \cos{(\varphi)}
$$
$$
y(\varphi) = r \sin{(\varphi)}
$$

### MCUA - Moviment Circular Uniformement Accelerat

Acceleració angular constant:

$$
\alpha = ct
$$

Velocitat angular constant:

$$
\omega(t) = \omega _0 + \alpha t
$$

Angle:

$$
\varphi(t) = \varphi _0 + \omega _0 t + \frac{1}{2} \alpha t^2
$$

Posició eix X i eix Y (on r és el radi de la circumferència que descriu la posició de l'objecte):

$$
x(\varphi) = r \cos{(\varphi)}
$$
$$
y(\varphi) = r \sin{(\varphi)}
$$

## Exercici 1: MCU – Moviment circular uniforme

**Objectiu**:  
Crear un objecte (el que tu vulguis) que es desplaci seguint un MCU en el pla XY.

**Condicions**:

- Posició inicial: $$(x_0,y_0,z_0)=(10,0,0)$$
- Velocitat angular: $$\omega = \frac{\pi}{2} rad/s$$
- Temps total: 30 segons (Actualitzeu el nombre de frames del visualitzador de 0 a 750 frames)

## Exercici 2: MCUA – Moviment circular uniformament accelerat

**Objectiu**:  
Crear un objecte que descrigui un MCUA en el pla XY. Observar que a partir del frame `220` aproximadament, sembla que l'objecte es desplaci en sentit contrari.

**Condicions**:

- Posició inicial: $$(x_0,y_0,z_0)=(10,0,0)$$
- Acceleració angular: $$\alpha = \frac{\pi}{2} rad/s^2$$
- Temps total: 30 segons (Actualitzeu el nombre de frames del visualitzador de 0 a 750 frames)ns

## Exercici 3: MCU + MRU

**Objectiu**:  
Crear un objecte (el que tu vulguis) que es desplaci seguint un MCU en el pla XY i un MRU en l'eix Z.

**Condicions**:

- Posició inicial: $$(x_0,y_0,z_0)=(10,0,0)$$
- Velocitat angular: $$\omega = \frac{\pi}{2} rad/s$$
- Velocitat lineal eix Z: $$2m/s$$
- Temps total: 30 segons (Actualitzeu el nombre de frames del visualitzador de 0 a 750 frames)

## Exercici 4: Tir parabòlic

**Objectiu**:  
Simular el moviment d’un objecte llançat en angle, generant una trajectòria parabòlica.

**Condicions**:

- Posició inicial: `(x₀, y₀, z₀) = (0, 0, 0)`
- Velocitat inicial: `v₀ = 10` unitats/s
- Angle de llançament: `α = 45°`
- Acceleració gravitatòria: `g = -9.81` unitats/s²
- Temps total: fins que arribi a `z=0`

## Exercici 5: Tir parabòlic amb angles diferents

**Objectiu**:  
Col·locar 5 objectes alineats a l’eix X i fer que cadascun realitzi un tir parabòlic amb el mateix valor de velocitat inicial però amb **angles diferents** de llançament.

**Condicions**:

- Velocitat inicial: `v₀ = 10` unitats/s
- Angles: `20°, 35°, 45°, 60°, 75°`
- Posició inicial dels objectes: `(x, y, z) = (-10, 0, 0), (-5, 0, 0), (0, 0, 0), (5, 0, 0), (10, 0, 0)`
- Acceleració gravitatòria: `g = -9.81` unitats/s²
- Durada de l’animació: fins que cada objecte arribi a `z=0`

## Exercici 6: Tir parabòlic amb velocitats inicials diferents

**Objectiu**:  
Col·locar 5 objectes alineats a l’eix X i fer que cadascun realitzi un tir parabòlic amb el **mateix angle de llançament** però amb **velocitats inicials diferents**.

**Condicions**:

- Angle de llançament: `α = 45°`
- Velocitats inicials: `5, 10, 15, 20, 25` unitats/s
- Posicions inicials dels objectes: `(x, y, z) = (-10, 0, 0), (-5, 0, 0), (0, 0, 0), (5, 0, 0), (10, 0, 0)`
- Acceleració gravitatòria: `g = -9.81` unitats/s²
- Durada de l’animació: fins que cada objecte arribi a `z=0`

## Codi base

```python
import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bloc = bpy.context.object

# Posar aquí condicions inicials: localització, velocitat, acceleració, angle...

# Condicions pel moviment amb Blender:
fps = bpy.context.scene.render.fps
interval = 1 / fps # En segons
duracio = 5 #segons. En alguns casos no es necessitarà.


for i in range(0, duracio * fps):  # Càlcul del moviment per cada fotograma de 0 al nombre total de fotogrames segons els segons de duració (duracio * fps). En alguns casos s'haurà de canviar el for per un altre tipus de bucle.

    t = i * interval
    # Actualització en el moviment de l'objecte utilitzant les formules adequades.

    bloc.keyframe_insert(data_path="location", frame=i) # Guardem a cada frame el canvi del moviment 
```
