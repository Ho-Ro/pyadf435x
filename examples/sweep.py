#!/usr/bin/env python3

from adf435x.interfaces import FX2
from adf435x.core import freq_make_regs
import time

intf = FX2()

while True:
    for freq in range(50, 100):
        regs = freq_make_regs(freq)
        intf.set_regs(regs[::-1])
        print('%0.1f MHz' % freq)
        time.sleep(0.1)
