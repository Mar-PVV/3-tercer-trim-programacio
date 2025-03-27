# Part Pràctica

## Exercici 1: Creació d'objectes primitius

**Objectiu**: Crear objectes primitius utilitzant operadors de la llibreria `bpy`.

**Instruccions**:

1. Crea un cub i col·loca'l a la posició `(0, 0, 0)`.
2. Crea una esfera UV i col·loca-la a la posició `(3, 0, 0)`.
3. Crea un cilindre amb un radi de 2 i una alçada de 5, i col·loca'l a la posició `(0, 3, 0)`.

Fes servir `bpy.ops.mesh.primitive_cube_add()`, `bpy.ops.mesh.primitive_uv_sphere_add()`, i `bpy.ops.mesh.primitive_cylinder_add()` per crear els objectes.

Fes captura de pantalla de la imatge obtinguda per tal de fer el README de la pràctica.

## Exercici 2: Modificar les propietats d'un objecte

**Objectiu**: Modificar les propietats d'un objecte primitiu afegit.

**Instruccions**:

1. Afegeix un cub a l'escena amb un costat de 2 unitats.
2. Modifica la ubicació del cub a `(1, 2, 0)`, la rotació a `(0, 0, 1.57)` i l'escala a `(1, 1, 0.5)`.

Utilitza `object.location`, `object.rotation_euler` i `object.scale`.

Fes captura de pantalla de la imatge obtinguda per tal de fer el README de la pràctica.

## Exercici 3: Animar un objecte

**Objectiu**: Crear una animació d’un cub que es desplaça de manera uniforme en línia recta.

**Instruccions**:

1. Afegeix un cub a l'escena.
2. Defineix la seva ubicació inicial com `(0, 0, 0)` en el fotograma 1.
3. Defineix la seva ubicació final com `(10, 0, 0)` en el fotograma 60.

Utilitza `obj.location` i `obj.keyframe_insert()` per animar l'objecte.

## Exercici 4: Animar múltiples objectes

**Objectiu**: Crear una animació d'un cub format per cubs.

**Instruccions**:

1. Afegeix 27 cubs en la posició (0,0,0). Crea una llista per tal de gestionar-los a tots.
2. Fes una animació per tal que es despleguin de manera que crein un cub format per cubs.

## Exercici 5: Càlcul dels fotogrames per segon

**Objectiu**: Calcular quants fotogrames es necessiten per fer un moviment amb una durada determinada.

**Instruccions**:

1. L'escena està configurada a 30 FPS.
2. Fes que un objecte es mogui des de `(0, 0, 0)` fins a `(10, 10, 10)` en 5 segons.
3. Calcula el nombre de fotogrames que calen per completar aquest moviment.
4. Crea una animació per moure l'objecte entre aquests punts en el nombre de fotogrames calculat.

**Pista**: Utilitza la fórmula `n = t * FPS` per calcular el nombre de fotogrames necessaris.

## Exercici 6: Crear una animació de rotació

**Objectiu**: Animar un cub per rotar-lo sobre l'eix Z.

**Instruccions**:

1. Afegeix un cub a l'escena.
2. Anima el cub per rotar-lo de `0` a `2 * pi` (360 graus) en 120 fotogrames.
3. Utilitza la funció `bpy.context.scene.render.fps` per gestionar la taxa de fotogrames per segon.

Fes servir `obj.rotation_euler` per modificar l'angle de rotació del cub.
