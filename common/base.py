#!/usr/bin/python3
# coding:utf8

import os


def checkPathExists(path):
    return os.path.exists(path)


def createFolder(path):
    if checkPathExists:
        return
    os.makedirs(path)
