import ast
from PIL import Image

with open("/home/hariharan/Desktop/Xiomara/fair-and-square/fair-and-square.txt","r") as f:
    data = f.read()

im = Image.new("RGB", (216,216))
data = ast.literal_eval(data)
im.putdata(data)
im.save("/home/hariharan/Desktop/Xiomara/fair-and-square/pixels.png")

