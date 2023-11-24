import pygerbv
import pandas

'''
Color is pixel, r, g, b floats [0,1]
alpha is float [0,1]
rotation is in radians -> 90 degrees = pi/2
translate is in inches
'''

layers = pandas.DataFrame([
    {"file": "Edge_Cuts-1.gm1", "alpha": 1, "color": (0, 1, 0, 0), "translate": (0,0), "rotate":3.14/2},
    {"file": "BoardOutline.gbr", "alpha": 1, "color": (0, 0, 1, 0), "translate": (2,5), "rotate": 0},
])

output = "output.svg"

proj = pygerbv.Project()
for _, line in layers.iterrows():
    layer = proj.open_layer_from_filename(line["file"])
    layer.alpha = line["alpha"]
    layer.color = line["color"]
    layer.translate(*line["translate"])
    layer.rotate(line["rotate"])
    print(layer.color)

assert(proj.files_loaded() == 2)  #  layer object returned and saved in the project
proj.export_auto_sized_svg_file(output)
