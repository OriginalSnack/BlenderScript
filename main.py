import bpy
import os

angle_x, angle_y, angle_z = 0, 0, 0
# Set the path to the folder where images will be saved
output_folder = "/Users/stanislavkravciv/Desktop/dataset/train"
os.makedirs(output_folder, exist_ok=True)

blender_file = "/Users/stanislavkravciv/blender_workspace/untitled.blend"

bpy.ops.wm.open_mainfile(filepath=blender_file)

bpy.context.scene.render.image_settings.file_format = 'JPEG'
bpy.context.scene.render.filepath = output_folder + "/image_"

num_screens = 10

for i in range(num_screens):
    bpy.context.scene.render.filepath = output_folder + "/image_{:04d}".format(i)

    angle_x += 1
    angle_y += 1
    angle_z += 1

    bpy.ops.render.render(write_still=True)

print(f"{num_screens} screens rendered and saved to {output_folder}")
