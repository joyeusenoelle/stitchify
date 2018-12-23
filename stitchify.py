""" Converts pixel-art images into cross-stitch patterns.

	This tool assumes that 1px = 1 stitch.

	TODO:
		* Accept image name from command line. (DONE)
		* Change characters to symbols for ease of reading.
		* Expand number of symbols.
		* Create image from symbolized pixels instead of just printing to screen. (DONE)
		* Add grid lines and edge labels to image. (DONE)
		* Add legend to image, based on the `symbols` dictionary. (DONE)
		* Correspond hex colors to floss colors, where possible.
		* (Maybe) add stitch count for each color. (DONE)
		* (Maybe) add GUI.
"""

__author__ = "Noëlle Anthony"
__version__ = "0.3.0"

import sys
from PIL import Image, ImageDraw
from collections import defaultdict

def main(img_name):
	img = Image.open(img_name)
	oimg_name_bits = img_name.split(".")
	oimg_name = "".join(oimg_name_bits[:-1]) + "_pattern." + oimg_name_bits[-1]

	w,h = img.size

	symbols = defaultdict(str)
	symbols["transparent"] = " "
	characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	symbol_counts = defaultdict(int)
#	l = 0
	lines = []
	for i in range(h):
		line = []
#		k = 0
		for j in range(w):
			c = "".join(["{}{}".format(hex(x//16).split('x')[-1], hex(x%16).split('x')[-1]) for x in list(img.getpixel((j,i)))])
			d = " "
			if c[-2:] == "ff":
				cs = c[:-2]
				if cs not in symbols.keys():
					symbols[cs] = characters[0]
					characters = characters[1:]
				symbol_counts[cs] += 1
				d = symbols[cs]
			line.append(d)
#			print(d, end="")
#			k += 1
#			if k == 9:
#				print("|", end="")
#				k = 0
		lines.append(line)
#		print()
#		l += 1
#		if l == 9:
#			for ww in range(int(w*1.1)+1):
#				if (ww+1)%10 == 0:
#					print("+", end="")
#				else:
#					print("-", end="")
#			l = 0
#			print()
	
#	print("\nLEGEND")
	legend = []
	keys = 0
	for k,v in symbols.items():
		if v != " ":
			keys += 1
			legend.append("{}: #{} ({}ct)".format(v, k, symbol_counts[k]))
	print("{} keys".format(keys))
#	print("\n".join(legend))

	owid, ohgt = (w*10)+10, (h*10)+10+(15*(int(keys/3)+1))
	print((owid, ohgt))
	oimg = Image.new("RGB", (owid, ohgt), "white")
	draw = ImageDraw.Draw(oimg)
	for ww in range(1, w+1):
		posx = ww * 10
		linecolor = 0 if posx % 100 == 0 else (128,128,128)
		linewidth = 2 if posx % 100 == 0 else 1
		draw.line((posx, 10, posx, (h*10)), fill=linecolor, width=linewidth)
	for hh in range(1, h+1):
		posy = hh * 10
		linecolor = 0 if posy % 100 == 0 else (128,128,128)
		linewidth = 2 if posx % 100 == 0 else 1
		draw.line((10, posy, owid, posy), fill=linecolor, width=linewidth)
	char_positions = [x*10+4 for x in range(1,h+1)]
#	print(char_positions)
	#char_colors = {" ": (0,0,0), "A": (0,0,0), "B": (128,0,0), "C": (0,128,0), "D": (0,255,255), "E": (128,128,0), "F": (128,0,128), "G": (0,0,0)}
	adjust = 0
	for line in lines:
		for char in range(len(line)):
			draw.text((char_positions[char], char_positions[0]-4+adjust), line[char], fill=0)
		adjust += 10
	legend_out = ""
	item_ct = 0
	for item in legend:
		item_ct += 1
		legend_out += item
		if item_ct % 3 == 0:
			legend_out += "\n"
		else:
			legend_out += "    "
	draw.text((20, (h*10)+10), legend_out, fill=0)
	oimg.save(oimg_name)
	print("Saved {}".format(oimg_name))


if __name__ == "__main__":
	#print(len(sys.argv))
	#print(sys.argv[1])
	if len(sys.argv) >= 2:
		img_name = sys.argv[1]
	else:
		img_name = "test.png"
	main(img_name)
