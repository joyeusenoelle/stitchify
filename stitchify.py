""" Converts pixel-art images into cross-stitch patterns.

	This tool assumes that 1px = 1 stitch.

	TODO:
		* Accept image name from command line.
		* Change characters to symbols for ease of reading.
		* Expand number of symbols.
		* Create image from symbolized pixels instead of just printing to screen.
		* Add grid lines and edge labels to image.
		* Add legend to image, based on the `symbols` dictionary.
		* Correspond hex colors to floss colors, where possible.
		* (Maybe) add stitch count for each color.
		* (Maybe) add GUI.
"""

__author__ = "Noëlle Anthony"
__version__ = "0.1.0"

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
		if c not in symbols.keys():
			symbols[c] = characters[0]
			characters = characters[1:]
		d = symbols[c]
		print(d, end="")
	print()
