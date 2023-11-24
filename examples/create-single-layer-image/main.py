import pygerbv

layer_name = "Edge_Cuts.gm1"
output = "output.svg"
color = (0, 1., 1., 0)  # pixel, red, green, blue. Scale is 0-1, actual output is 0-255 with 1 giving 255.
alpha = 1  # 0-1 float

proj = pygerbv.Project()
layer = proj.open_layer_from_filename(layer_name)
assert(proj.files_loaded() == 1)  #  layer object returned and saved in the project
layer.alpha = alpha
layer.color = color
print(layer.color)
proj.export_auto_sized_svg_file(output)

