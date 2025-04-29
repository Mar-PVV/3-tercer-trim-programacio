import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
bloc = bpy.context.object

bpy.ops.mesh.primitive_cube_add(location=(0,2,0))
bloc1 = bpy.context.object

x0 = 0
v1 = 2
v2 = 4 

# Condicions pel moviment amb Blender:
fps = bpy.context.scene.render.fps
interval = 1 / fps # En segons
duracio = 5 #segons. En alguns casos no es necessitarà.


for i in range(0, duracio * fps):  # Càlcul del moviment per cada fotograma de 0 al nombre total de fotogrames segons els segons de duració (duracio * fps). En alguns casos s'haurà de canviar el for per un altre tipus de bucle.

    t = i * interval
    
    bloc.location.x = x0 + v1 * t
    bloc.keyframe_insert(data_path="location", frame=i)
    bloc1.location.x = x0 + v2 * t
    bloc1.keyframe_insert(data_path="location", frame=i)