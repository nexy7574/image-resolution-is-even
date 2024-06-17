from pathlib import Path

import pytest
from image_resolution_is_even import *

# Oh my god.


assets = Path(__file__).parent / "assets"
_7x8_png = str((assets / "7x8.png").resolve().relative_to(Path.cwd()))
_8x7_png = str((assets / "8x7.png").resolve().relative_to(Path.cwd()))
_8x8_png = str((assets / "8x8.png").resolve().relative_to(Path.cwd()))


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, False),
        (_8x7_png, True),
        (_8x8_png, True),
    ],
)
def test_image_width_is_even(image_path, expected):
    assert image_width_is_even(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, True),
        (_8x7_png, False),
        (_8x8_png, False),
    ],
)
def test_image_width_is_odd(image_path, expected):
    assert image_width_is_odd(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, True),
        (_8x7_png, False),
        (_8x8_png, True),
    ],
)
def test_image_height_is_even(image_path, expected):
    assert image_height_is_even(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, False),
        (_8x7_png, True),
        (_8x8_png, False),
    ],
)
def test_image_height_is_odd(image_path, expected):
    assert image_height_is_odd(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, False),
        (_8x7_png, False),
        (_8x8_png, True),
    ],
)
def test_image_resolution_is_even(image_path, expected):
    assert image_resolution_is_even(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, True),
        (_8x7_png, True),
        (_8x8_png, False),
    ],
)
def test_image_resolution_is_odd(image_path, expected):
    assert image_resolution_is_odd(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 8),
        (_8x7_png, 8),
        (_8x8_png, 8),
    ],
)
def test_even_image_height_ciel(image_path, expected):
    assert even_image_height_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 8),
        (_8x7_png, 6),
        (_8x8_png, 8),
    ],
)
def test_even_image_height_floor(image_path, expected):
    assert even_image_height_floor(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 8),
        (_8x7_png, 8),
        (_8x8_png, 8),
    ],
)
def test_even_image_width_ciel(image_path, expected):
    assert even_image_width_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 6),
        (_8x7_png, 8),
        (_8x8_png, 8),
    ],
)
def test_even_image_width_floor(image_path, expected):
    assert even_image_width_floor(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, (8, 8)),
        (_8x7_png, (8, 8)),
        (_8x8_png, (8, 8)),
    ],
)
def test_even_image_resolution_ciel(image_path, expected):
    assert even_image_resolution_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, (6, 8)),
        (_8x7_png, (8, 6)),
        (_8x8_png, (8, 8)),
    ],
)
def test_even_image_resolution_floor(image_path, expected):
    assert even_image_resolution_floor(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 9),
        (_8x7_png, 7),
        (_8x8_png, 9),
    ],
)
def test_odd_image_height_ciel(image_path, expected):
    assert odd_image_height_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 7),
        (_8x7_png, 7),
        (_8x8_png, 7),
    ],
)
def test_odd_image_height_floor(image_path, expected):
    assert odd_image_height_floor(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 7),
        (_8x7_png, 9),
        (_8x8_png, 9),
    ],
)
def test_odd_image_width_ciel(image_path, expected):
    assert odd_image_width_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, 7),
        (_8x7_png, 7),
        (_8x8_png, 7),
    ],
)
def test_odd_image_width_floor(image_path, expected):
    assert odd_image_width_floor(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, (7, 9)),
        (_8x7_png, (9, 7)),
        (_8x8_png, (9, 9)),
    ],
)
def test_odd_image_resolution_ciel(image_path, expected):
    assert odd_image_resolution_ciel(image_path) == expected


@pytest.mark.parametrize(
    "image_path, expected",
    [
        (_7x8_png, (7, 7)),
        (_8x7_png, (7, 7)),
        (_8x8_png, (7, 7)),
    ],
)
def test_odd_image_resolution_floor(image_path, expected):
    assert odd_image_resolution_floor(image_path) == expected
