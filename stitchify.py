from PIL import Image
from collections import defaultdict

img = Image.open('test.png')

w,h = img.size

symbols = defaultdict(str)
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(h):
	for j in range(w):
		c = "".join(["{}{}".format(hex(x//16).split('x')[-1], hex(x%16).split('x')[-1]) for x in list(img.getpixel((j,i)))])
		d = " "
		if c in symbols.keys():
			d = symbols[c]
		else:
			symbols[c] = characters[0]
			characters = characters[1:]
			d = symbols[c]
		print(d, end="")
	print()
