# -*- coding: utf-8 -*-
import pkg_resources
from .extractor import *

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'