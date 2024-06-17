# image-resolution-is-even

> Check whether an image's resolution is even or not.

*Note: This README is "inspired" by [is-even](https://www.npmjs.com/package/is-even). In fact, so is the entire project.

## Install

Install with [pip](https://pypi.org/project/pip/):

```sh
 pip install -i https://test.pypi.org/simple/ image-resolution-is-even
```

## Usage

```pycon
>>> from image_resolution_is_even import *
>>> image_resolution_is_even('path/to/image.jpg')
True
>>> image_resolution_is_odd('path/to/image.jpg')
False
>>> image_width_is_even('path/to/image.jpg')
True
>>> image_width_is_odd('path/to/image.jpg')
False
>>> image_height_is_even('path/to/image.jpg')
True
>>> image_height_is_odd('path/to/image.jpg')
False
>>> even_image_height_ciel('path/to/image.jpg')
258
>>> even_image_width_ciel('path/to/image.jpg')
258
>>> even_image_height_floor('path/to/image.jpg')
256
>>> even_image_width_floor('path/to/image.jpg')
256
>>> even_image_resolution_ciel('path/to/image.jpg')
(258, 258)
>>> even_image_resolution_floor('path/to/image.jpg')
(256, 256)  
>>> odd_image_height_floor('path/to/image.jpg')
257
>>> odd_image_width_floor('path/to/image.jpg')
257
>>> odd_image_height_ciel('path/to/image.jpg')
259
>>> odd_image_width_ciel('path/to/image.jpg')
259
>>> odd_image_resolution_floor('path/to/image.jpg')
(257, 257)
>>> odd_image_resolution_ciel('path/to/image.jpg')
(259, 259)
```

## About

### Contributing

Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](../../issues/new).

### License

Released under the [MIT License](LICENSE).
