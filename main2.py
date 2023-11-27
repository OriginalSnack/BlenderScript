import bpy
import os
import math

angle_x, angle_y, angle_z = 0, 0, 0

object_to_rotate = bpy.context.scene.objects.get("SHAHED_PAINT_obj")

output_folder = "/Users/stanislavkravciv/Desktop/dataset/train/images"

blender_file = "/Users/stanislavkravciv/blender_workspace/untitled1.blend"
bpy.ops.wm.open_mainfile(filepath=blender_file)

bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = output_folder + "/image_"

num_screens = 10

for i in range(num_screens):
    bpy.context.scene.render.filepath = output_folder + "/image_{:04d}".format(i)

    object_to_rotate.rotation_euler = (math.radians(angle_x), math.radians(angle_y), math.radians(angle_z))

    angle_x += 1
    angle_y += 1
    angle_z += 1

    bpy.ops.render.render(write_still=True)

print(f"{num_screens} screens rendered and saved to {output_folder}")