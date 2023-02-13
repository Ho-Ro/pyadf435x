#!/usr/bin/env python

# requires the new fx2 firmware (based on libfx2)
# store current register settings as default for power-on

from adf435x.interfaces import FX2

FX2().store_default()
