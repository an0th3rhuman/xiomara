from PIL import Image
im = Image.open("/home/hariharan/Desktop/Xiomara/fair-and-square/pixels.ppm")
pixels = list(im.getdata())

with open("/home/hariharan/Desktop/Xiomara/fair-and-square/fair-and-square.txt","w") as f:
    f.write(str(pixels))
