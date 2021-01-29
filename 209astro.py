from PIL import Image, ImageFilter


img = Image.open('./pics/astro.jpg')

img_w = img.size[0]
img_h = img.size[1]

new_size = (500, int(500 * img_h / img_w))

new_img = img.resize(new_size)
new_img.save('./pics/astro_new.png', 'png')

img.thumbnail((300, 300))
img.save('./pics/astro_thumb.jpg')

new_img.show()
