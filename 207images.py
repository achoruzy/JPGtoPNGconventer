from PIL import Image, ImageFilter

img = Image.open('./pics/pikachu.jpg')

filtered_img = img.convert('L')
filtered_img = filtered_img.rotate(90)
filtered_img = filtered_img.resize((500, 500))

box = (100, 100, 400, 400)
filtered_img = filtered_img.crop(box)
filtered_img.save("gray.png", 'png')
filtered_img.show()
