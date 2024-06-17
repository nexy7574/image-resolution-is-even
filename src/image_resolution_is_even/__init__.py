from os import PathLike
from pathlib import Path
from typing import BinaryIO, Union as U

from PIL import Image

IMAGE_TYPE: U['PathLike', Path, str, BinaryIO, Image.Image] = U[PathLike, Path, str, BinaryIO, Image.Image]

__all__ = (
    "image_width_is_even",
    "image_height_is_even",
    "image_width_is_odd",
    "image_height_is_odd",
    "image_resolution_is_even",
    "image_resolution_is_odd",
    "even_image_height_ciel",
    "even_image_width_ciel",
    "odd_image_height_floor",
    "odd_image_width_floor",
    "even_image_resolution_ciel",
    "even_image_resolution_floor",
    "odd_image_resolution_ciel",
    "odd_image_resolution_floor",
    "even_image_height_floor",
    "odd_image_width_ciel",
    "odd_image_height_ciel",
    "even_image_width_floor",
    "IMAGE_TYPE"
)

__author__ = "nexy7574 <https://github.com/nexy7574>"
__source__ = "https://github.com/nexy7574/image_resolution_is_even"


def __load_image(image_path: "IMAGE_TYPE") -> Image.Image:
    if isinstance(image_path, Image.Image):
        return image_path
    return Image.open(image_path)


def image_width_is_even(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the WIDTH (length) of the image is an even number.

    :param image: The image object to check.
    :return: bool - True if the width is even, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return image.width % 2 == 0


def image_height_is_even(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the HEIGHT (length) of the image is an even number.

    :param image: The image object to check.
    :return: bool - True if the height is even, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return image.height % 2 == 0


def image_width_is_odd(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the WIDTH (length) of the image is an odd number.

    :param image: The image object to check.
    :return: bool - True if the width is odd, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return not image_width_is_even(image)


def image_height_is_odd(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the HEIGHT (length) of the image is an odd number.

    :param image: The image object to check.
    :return: bool - True if the height is odd, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return not image_height_is_even(image)


def image_resolution_is_even(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the resolution of the image is even.

    :param image: The image object to check.
    :return: bool - True if the resolution is even, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return image_width_is_even(image) and image_height_is_even(image)


def image_resolution_is_odd(image: "IMAGE_TYPE") -> bool:
    """
    Checks if the resolution of the image is odd.

    :param image: The image object to check.
    :return: bool - True if the resolution is odd, False otherwise.
    :rtype: bool
    """
    image = __load_image(image)
    return not image_resolution_is_even(image)


def even_image_height_ciel(image: "IMAGE_TYPE") -> int:
    """
    Returns the next even number greater than or equal to the image height.

    :param image: The image object to check.
    :return: int - The next even number greater than or equal to the image height.
    :rtype: int
    """
    image = __load_image(image)
    return image.height if image_height_is_even(image) else image.height + 1


def even_image_height_floor(image: "IMAGE_TYPE") -> int:
    """
    Returns the next even number less than or equal to the image height.

    :param image: The image object to check.
    :return: int - The next even number less than or equal to the image height.
    :rtype: int
    """
    image = __load_image(image)
    return image.height if image_height_is_even(image) else image.height - 1


def even_image_width_ciel(image: "IMAGE_TYPE") -> int:
    """
    Returns the next even number greater than or equal to the image width.

    :param image: The image object to check.
    :return: int - The next even number greater than or equal to the image width.
    :rtype: int
    """
    image = __load_image(image)
    return image.width if image_width_is_even(image) else image.width + 1


def even_image_width_floor(image: "IMAGE_TYPE") -> int:
    """
    Returns the next even number less than or equal to the image width.

    :param image: The image object to check.
    :return: int - The next even number less than or equal to the image width.
    :rtype: int
    """
    image = __load_image(image)
    return image.width if image_width_is_even(image) else image.width - 1


def odd_image_height_floor(image: "IMAGE_TYPE") -> int:
    """
    Returns the next odd number less than or equal to the image height.

    :param image: The image object to check.
    :return: int - The next odd number less than or equal to the image height.
    :rtype: int
    """
    image = __load_image(image)
    return image.height if image_height_is_odd(image) else image.height - 1


def odd_image_width_ciel(image: "IMAGE_TYPE") -> int:
    """
    Returns the next odd number greater than or equal to the image width.

    :param image: The image object to check.
    :return: int - The next odd number greater than or equal to the image width.
    :rtype: int
    """
    image = __load_image(image)
    return image.width if image_width_is_odd(image) else image.width + 1


def odd_image_width_floor(image: "IMAGE_TYPE") -> int:
    """
    Returns the next odd number less than or equal to the image width.

    :param image: The image object to check.
    :return: int - The next odd number less than or equal to the image width.
    :rtype: int
    """
    image = __load_image(image)
    return image.width if image_width_is_odd(image) else image.width - 1


def odd_image_height_ciel(image: "IMAGE_TYPE") -> int:
    """
    Returns the next odd number greater than or equal to the image height.

    :param image: The image object to check.
    :return: int - The next odd number greater than or equal to the image height.
    :rtype: int
    """
    image = __load_image(image)
    return image.height if image_height_is_odd(image) else image.height + 1


def even_image_resolution_ciel(image: "IMAGE_TYPE") -> tuple[int, int]:
    """
    Returns the next even number greater than or equal to the image resolution.

    :param image: The image object to check.
    :return: tuple[int, int] - The next even number greater than or equal to the image resolution.
    :rtype: tuple[int, int]
    """
    image = __load_image(image)
    return even_image_width_ciel(image), even_image_height_ciel(image)


def even_image_resolution_floor(image: "IMAGE_TYPE") -> tuple[int, int]:
    """
    Returns the next even number less than or equal to the image resolution.

    :param image: The image object to check.
    :return: tuple[int, int] - The next even number less than or equal to the image resolution.
    :rtype: tuple[int, int]
    """
    image = __load_image(image)
    return even_image_width_floor(image), even_image_height_floor(image)


def odd_image_resolution_ciel(image: "IMAGE_TYPE") -> tuple[int, int]:
    """
    Returns the next odd number greater than or equal to the image resolution.

    :param image: The image object to check.
    :return: tuple[int, int] - The next odd number greater than or equal to the image resolution.
    :rtype: tuple[int, int]
    """
    image = __load_image(image)
    return odd_image_width_ciel(image), odd_image_height_ciel(image)


def odd_image_resolution_floor(image: "IMAGE_TYPE") -> tuple[int, int]:
    """
    Returns the next odd number less than or equal to the image resolution.

    :param image: The image object to check.
    :return: tuple[int, int] - The next odd number less than or equal to the image resolution.
    :rtype: tuple[int, int]
    """
    image = __load_image(image)
    return odd_image_width_floor(image), odd_image_height_floor(image)
