from __future__ import annotations

import argparse


def real_main(args: argparse.Namespace):
    print(f"args: {args}")
    import pykpc.ffi

    pykpc.ffi


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="pykpc")
    return parser


def main():
    real_main(get_arg_parser().parse_args())


if __name__ == "__main__":
    main()
