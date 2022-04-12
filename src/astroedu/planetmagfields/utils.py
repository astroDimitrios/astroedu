#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import os
from importlib_resources import files

# stdDatDir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data/')
stdDatDir = files('astroedu.planetmagfields').joinpath('data/')

planetlist = ["mercury", "earth", "jupiter", "saturn", "uranus", "neptune",
              "ganymede"]