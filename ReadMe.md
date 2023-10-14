libzip.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=========
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/libzip.py/workflows/CI/master/libzip-0.CI-py3-none-any.whl)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/libzip.py.svg)](https://libraries.io/github/KOLANICH-libs/libzip.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/libzip.py, grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

Python ctypes-based bindings to [`libzip`](https://github.com/nih-at/libzip). You need a `libzip` installed:
* `libzip4` in Debian-based distros.
* `libzip` in RPM-based distros, Arch, and Gentoo.

**Warning: Currently `libzip` is used for updating files witin the archive. It doesn't allow rewriting files in archives without creating a copy of the archive. [It is considered contradicting `libzip` goals by its authors.](https://github.com/nih-at/libzip/issues/304)**. We need a lib allowing to do that.

For the docs see [the tutorial](./tutorial.ipynb)[![NBViewer](https://nbviewer.org/static/ico/ipynb_icon_16x16.png)](https://nbviewer.org/urls/codeberg.org/KOLANICH-libs/libzip.py/raw/branch/master/tutorial.ipynb).
