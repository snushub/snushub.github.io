from PIL import Image, ImageDraw

# Things I have to do to make this project work
# -> store arc start and end values
# -> convert "normal" coordinates to pillow coordinates
# -> Know how many steps until peak
# -> Figure out how to draw the peak
# -> Figure out how to use offsets
# -> make the images nice

th = 4

w, h = 400, 400
shape = [(290, 200), (390, 400)]
shape2 = [(300, 0 + th), (400, 200 + th)]
shape3 = [(290 + 50, 200 + 2), (340 + 10, 200 + 2)]
# creating new Image object
img = Image.new("RGB", (w, h))

# create rectangle image
img1 = ImageDraw.Draw(img)
img1.arc(shape, start=180, end=270, fill="pink", width=5)

img1.arc(shape2, start=0, end=90, fill="pink", width=5)

img1.line(shape3, fill="pink", width=5)

img.save("this.png")
