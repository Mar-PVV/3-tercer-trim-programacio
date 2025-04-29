import bpy
import math

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

bpy.ops.mesh.primitive_cube_add(location=(10,0,0))
bloc = bpy.context.object

w = 10 * math.pi 
r = 10

# Condicions pel moviment amb Blender:
fps = bpy.context.scene.render.fps
interval = 1 / fps # En segons
duracio = 30 #segons. En alguns casos no es necessitarà.


for i in range(0, duracio * fps):  # Càlcul del moviment per cada fotograma de 0 al nombre total de fotogrames segons els segons de duració (duracio * fps). En alguns casos s'haurà de canviar el for per un altre tipus de bucle.

    t = i * interval
    
    phi = w * t
    
    bloc.location.x = r * math.cos(phi)
    bloc.location.y = r * math.sin(phi)
    bloc.keyframe_insert(data_path="location", frame=i)