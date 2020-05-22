from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpeg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
# print(img)