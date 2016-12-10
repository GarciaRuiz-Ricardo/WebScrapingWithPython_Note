from PIL import Image, ImageFilter

kitten = Image.open('5.1.logo.jpg')
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save('5.1.logo_blurred.jpg')
blurryKitten.show()