from . import *
from . import __all__
import argparse


def main():
    parser = argparse.ArgumentParser(description='Check if an image resolution is even')
    parser.add_argument('image_path', type=str, help='Path to an image file')
    parser.add_argument("--as-json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    results = {}
    for func in __all__:
        if func == "IMAGE_TYPE":
            continue
        func = getattr(__import__(__name__), func)
        if callable(func) and not isinstance(func, type):
            try:
                results[func.__name__] = func(args.image_path)
            except TypeError as e:
                results[func.__name__] = e

    if args.as_json:
        import json
        print(json.dumps(results, default=str))
    else:
        for func, result in results.items():
            print(f"{func}: {result}")


if __name__ == "__main__":
    main()
