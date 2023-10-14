import ctypes.util
import glob
import os.path
import platform
import re
from warnings import warn

warn("We have moved from M$ GitHub to https://codeberg.org/KOLANICH-libs/libzip.py, read why on https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo .")

from .enums import *

ZIP_UINT16_MAX = 0xFFFF
ZIP_EXTRA_FIELD_ALL = ZIP_UINT16_MAX
ZIP_EXTRA_FIELD_NEW = ZIP_UINT16_MAX
