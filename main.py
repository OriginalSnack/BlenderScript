import bpy
import math

def screanshots(out_path, i):
    bpy.context.scene.render.image_settings.file_format = 'JPEG'

    bpy.context.scene.render.filepath = output_path + "/image_{:04d}".format(i)

    bpy.ops.render.render(write_still=True)


shahed = "W"
camera = "Camera"

amount_of_photos = 4

output_path = "/Users/stanislavkravciv/Desktop/dataset/test"

obj = bpy.data.objects.get(shahed)
obj_camera = bpy.data.objects.get(camera)

for i in range(amount_of_photos):
    screanshots(output_path, i)
    if obj is not None:
        obj.rotation_euler[0] += 0.1
        obj.rotation_euler[1] += 0.1
        obj.rotation_euler[2] += 0.1
