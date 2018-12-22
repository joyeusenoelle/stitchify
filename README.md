# stitchify
Convert pixel art to cross-stitch patterns

Requires Python 3, PIL

This tool assumes that 1px = 1 stitch.

I'm deliberately not randomizing the symbols. Sending the same input image should result in the same output image every time.

TODO:
* Accept image name on command line.
* Change characters to symbols for ease of reading.
* Expand number of symbols.
* Create image from symbolized pixels instead of just printing to screen.
* Add grid lines and edge labels to image.
* Add legend to image, based on the `symbols` dictionary.
* Correspond hex colors to floss colors, where possible.
* (Maybe) add stitch count for each color.
* (Maybe) add GUI.
