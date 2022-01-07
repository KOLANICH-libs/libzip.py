libzip.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=========
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/libzip.py/workflows/CI/master/libzip-0.CI-py3-none-any.whl)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/libzip.py.svg)](https://libraries.io/github/KOLANICH-libs/libzip.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

Python ctypes-based bindings to [`libzip`](https://github.com/nih-at/libzip). You need a `libzip` installed:
* `libzip4` in Debian-based distros.
* `libzip` in RPM-based distros, Arch, and Gentoo.

**Warning: Currently `libzip` is used for updating files witin the archive. It doesn't allow rewriting files in archives without creating a copy of the archive. [It is considered contradicting `libzip` goals by its authors.](https://github.com/nih-at/libzip/issues/304)**. We need a lib allowing to do that.

For the docs see [the tutorial](./tutorial.ipynb)[![NBViewer](https://nbviewer.org/static/ico/ipynb_icon_16x16.png)](https://nbviewer.org/urls/codeberg.org/KOLANICH-libs/libzip.py/raw/branch/master/tutorial.ipynb).
