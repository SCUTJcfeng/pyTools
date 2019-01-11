#!/usr/bin/python3
# -*- coding:utf-8 –*-

import time
import threading

thCount = 0


def thrLimit(name='default', limit=1):
    def decorator(f):
        def wrapper(*args, **kwargs):
            while True:
                thList = threading.enumerate()
                count = 0
                for thr in thList:
                    if thr.name.find(name) != -1:
                        count += 1
                if count < limit:
                    break
                time.sleep(2)
            global thCount
            thrName = name + str(thCount)
            thCount += 1
            thr = threading.Thread(target=f, name=thrName, args=args, kwargs=kwargs)
            thr.start()
        return wrapper
    return decorator


def asyncDec(f):
    def wrapper(*args, **kwargs):
        thr = threading.Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper
