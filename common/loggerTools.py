#!/usr/bin/python3
# -*- coding:utf-8 –*-

import logging
from .base import createFolder, getPathDirName


class Logger():
    def __init__(self, logPath=None, console=True):
        logger = logging.getLogger()
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
            if logPath is not None:
                createFolder(getPathDirName(logPath))
                handler = logging.FileHandler(logPath, encoding='utf-8')
                handler.setFormatter(formatter)
                logger.addHandler(handler)
            if console is True:
                consoleHandle = logging.StreamHandler()
                consoleHandle.setFormatter(formatter)
                logger.addHandler(consoleHandle)
        self.logger = logger

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
