# Pràctica 5: Cinètica amb Python i Blender

## Fórmules de referència

Atenció! Com que treballem en tres dimensions, recorda que l'eix associat amb l'alçada és l'eix `Z`.

### MRU - Moviment Rectilini Uniforme

$$
x(t) = x_0 + v \cdot t
$$

### MRUA - Moviment Rectilini Uniformement Accelerat

$$
x(t) = x_0 + v_0 \cdot t + \frac{1}{2} a \cdot t^2
$$

O `y` si volem moure-ho en l'eix `Y`.

#### Cas particular: Caiguda lliure

$$
z(t) = z_0 + \frac{1}{2} g \cdot t^2
$$

On aproximant l'acceleració gravitatòria és aproximadament: $$g=-9,81$$

### Tir parabòlic

$$
x(t) = x_0 + v_{0x} \cdot t
$$
$$
z(t) = z_0 + v_{0z} \cdot t + \frac{1}{2} g \cdot t^2
$$
$$
v_{0x} = v_0 \cdot \cos{\alpha}
$$
$$
v_{0z} = v_0 \cdot \sin{\alpha}
$$

On $\alpha$ és l'angle de llançament.

## Exercici 1: MRU – Moviment rectilini uniforme

**Objectiu**:  
Crear un objecte (el que tu vulguis) que es desplaci en línia recta amb velocitat constant al llarg de l’eix X.

**Condicions**:

- Posició inicial: `x₀ = 0`
- Velocitat: `v = 2` unitats/s
- Temps total: `5` segons

## Exercici 2: MRUA – Moviment rectilini uniformament accelerat

**Objectiu**:  
Crear un objecte que s’acceleri al llarg de l’eix Y, partint del repòs.

**Condicions**:

- Posició inicial: `y₀ = 7`
- Velocitat inicial: `v₀ = 0`
- Acceleració: `a = 1.5` unitats/s²
- Temps total: `4` segons

## Exercici 3: Caiguda lliure

**Objectiu**:  
Simular la caiguda d’un objecte a causa de la gravetat, sense velocitat inicial.

**Condicions**:

- Posició inicial: `(x₀, y₀, z₀) = (0, 0, 10)`
- Acceleració gravitatòria: `g = -9.81` unitats/s²
- Temps total: fins que arribi a `z=0`

**Ampliació**:

- Prova-ho per altres alçades per comprovar que para un cop arriba a `z=0`.

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
