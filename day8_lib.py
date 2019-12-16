import logging
from functools import reduce
from itertools import starmap

from util import flatten, grouper

LOG = logging.getLogger(__name__)

BLACK = "0"
WHITE = "1"
TRANSPARENT = "2"
OPAQUE = [BLACK, WHITE]

def number_of_zeros_in_layer(layer):
    return sum(1 for digit in flatten(layer) if int(digit) == 0)


def compute_checksu(layer):
    digits = [int(i) for i in flatten(layer)]
    num_ones = sum(1 for i in digits if i == 1)
    num_twos = sum(1 for i in digits if i == 2)
    return num_ones * num_twos

def compute_checksum(heigth, width, input_string):

    rows = grouper(input_string, width)
    layers = grouper(rows, heigth)

    layers = list(layers)
    LOG.debug(layers)
    idx_zeros_and_checksum = ((idx, number_of_zeros_in_layer(layer), compute_checksu(layer)) for idx, layer in enumerate(layers))
    idx_zeros_and_checksum = list(idx_zeros_and_checksum)
    LOG.debug(idx_zeros_and_checksum)
    idx, num_zeros, checksum = min(idx_zeros_and_checksum, key=lambda s: s[1])
    LOG.debug(f"Layer {idx=} with {num_zeros} zeros has checksum {checksum}")
    return checksum

def pick_first_pixel_if_opaque(a,b):
    LOG.debug(f"comparing PIXELS  layers {a} and {b}")
    return a if a in OPAQUE else b

def render_from_two_layers(top, bottom):
    LOG.debug(f"comparing flat layers {top} and {bottom}")
    pixels_pairwise = zip(top,bottom)
    return starmap(pick_first_pixel_if_opaque,pixels_pairwise)

def render_image(height, width, input_string):
    flat_layers = grouper(input_string, width*height)
    redering = reduce(render_from_two_layers, flat_layers)
    render = list(map(list,grouper(map(int,redering),width)))
    return render
