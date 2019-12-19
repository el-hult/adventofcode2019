from typing import Literal, List

import nose
from day8_lib import compute_checksum, render_image


def test1():
    IMAGE_TALL = 2
    IMAGE_WIDTH = 3
    MY_INPUT = "123456789012"
    checksum_a = compute_checksum(IMAGE_TALL, IMAGE_WIDTH, MY_INPUT)
    nose.tools.assert_equal(checksum_a,1)


def test2():
    IMAGE_TALL = 2
    IMAGE_WIDTH = 2
    MY_INPUT = "0222112222120000"
    image_matrix: List[List[Literal[0,1,2]]] = render_image(IMAGE_TALL, IMAGE_WIDTH, MY_INPUT)
    nose.tools.assert_equal(image_matrix,[[0,1],[1,0]])
