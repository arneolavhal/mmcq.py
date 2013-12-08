#! -*- coding: utf-8 -*-
from .quantize import mmcq

__version__ = (0, 0, 1)


def get_palette(image, color_count=10, quality=1):
    colors = []
    for y in xrange(0, image.size[1]):
        for x in xrange(0, image.size[0], quality):
            r, g, b = image.getpixel((x, y))
            if r < 250 and g < 250 and b < 250:
                colors.append((r, g, b))

    c_map = mmcq(colors, color_count)
    return c_map.palette
