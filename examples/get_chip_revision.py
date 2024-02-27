#!/usr/bin/env python

# requires the new fx2 firmware (based on libfx2)

from adf435x.interfaces import FX2

intf = FX2()

rev = intf.get_chip_rev()[0]
print( 'FX2 chip revision:', rev )

