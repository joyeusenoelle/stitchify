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

import sys
from PIL import Image
from collections import defaultdict

def main(img_name):
	img = Image.open(img_name)

	w,h = img.size

	symbols = defaultdict(str)
	symbols["transparent"] = " "
	characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	l = 0
	for i in range(h):
		k = 0
		for j in range(w):
			c = "".join(["{}{}".format(hex(x//16).split('x')[-1], hex(x%16).split('x')[-1]) for x in list(img.getpixel((j,i)))])
			d = " "
			if c[-2:] == "ff":
				cs = c[:-2]
				if cs not in symbols.keys():
					symbols[cs] = characters[0]
					characters = characters[1:]
				d = symbols[cs]
			print(d, end="")
			k += 1
			if k == 9:
				print("|", end="")
				k = 0
		print()
		l += 1
		if l == 9:
			for ww in range(int(w*1.1)+1):
				if (ww+1)%10 == 0:
					print("+", end="")
				else:
					print("-", end="")
			l = 0
			print()
	
	print("\nLEGEND")
	for k,v in symbols.items():
		print("{}: #{}".format(v,k))

if __name__ == "__main__":
	#print(len(sys.argv))
	#print(sys.argv[1])
	if len(sys.argv) >= 2:
		img_name = sys.argv[1]
	else:
		img_name = "test.png"
	main(img_name)
