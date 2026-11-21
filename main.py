#!/usr/bin/env python3
"""Republic of Pluvia - passport spread entry.

Copies the bundled artwork to /output/entry.png byte-for-byte.
Standard library only, no network, deterministic: the output bytes
are exactly the artwork bytes on every run.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ARTWORK = os.path.join(HERE, "artwork.png")
EXPECTED_SHA256 = "7fa20e0b4156dba7fda3d659be97f47b46ca082b557e241e71726ac0740d7c9f"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def check_png(path):
    """Return (width, height, size) after verifying the PNG signature."""
    size = os.path.getsize(path)
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("artwork is not a PNG")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height, size


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    shutil.copyfile(ARTWORK, out_path)
    digest = sha256_of(out_path)
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    width, height, size = check_png(out_path)
    if (width, height) != (1024, 1024) or size > 1048576:
        print(f"bad output: {width}x{height} {size} bytes", file=sys.stderr)
        return 1
    print(f"wrote {out_path} sha256={digest} size={size} dims={width}x{height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
