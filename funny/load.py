#!/usr/bin/python3
# -*- coding:utf-8 –*-

import time
from collections import deque


load = deque('>-----------------------')

while True:
    print("".join(load), end='\r')
    load.rotate(1)
    time.sleep(0.08)
