# Pràctica 6: Moviment circular amb Python i Blender

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

## Exercici 4: Efecte roda de vagó

Llegir el següent [link](https://ca.wikipedia.org/wiki/Efecte_estrobosc%C3%B2pic#Efecte_roda_de_vag%C3%B3).

**Objectiu**:  
Crear quatre objectes, un de color diferenciat, que es desplacin seguint un MCU en el pla XY. Anar augmentant la velocitat angular fins a observar l'efecte roda de vagó, entre d'altres.

**Condicions**:

- Posició inicial dels quatre objectes:

$$(x_0,y_0,z_0)=(10,0,0)$$
$$(x_0,y_0,z_0)=(0,10,0)$$
$$(x_0,y_0,z_0)=(-10,0,0)$$
$$(x_0,y_0,z_0)=(0,-10,0)$$

- L'objecte de la posició `(10,0,0)` de color diferent:

```python
mat = bpy.data.materials.new("PKHG")
mat.diffuse_color = (1.0,0.0,0.0, 1.0) # (Vermell,Verd,Blau,Opacitat) - Valors del 0 a l'1.

bpy.ops.mesh.primitive_cube_add(location=(10,0,0))
bloc1 = bpy.context.object
bloc1.active_material = mat
```

- Velocitat angular: $$\omega = \frac{\pi}{2} rad/s$$
- Temps total: 30 segons (Actualitzeu el nombre de frames del visualitzador de 0 a 750 frames)
