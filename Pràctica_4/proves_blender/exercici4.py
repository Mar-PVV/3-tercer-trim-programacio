import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=True)

num_cubs = 3
llista_cubs = []

for i in range(num_cubs):
    for j in range(num_cubs):
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        cub = bpy.context.object
        cub.keyframe_insert(data_path="location", frame=1)
        cub.location = (i*2,j*2,0)
        cub.keyframe_insert(data_path="location", frame=60)
        llista_cubs.append(cub)