#!/usr/bin/python3
# -*- coding:utf-8 –*-

import datetime
from dateutil.parser import parse


def todayDatetime():
    return datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


def convertStrToTs(timeStr, timeFormat="%y-%m-%d %H:%M"):
    date = datetime.datetime.strptime(timeStr, timeFormat)
    return int(date.timestamp() * 1000)


def convertTsToStr(ts, timeFormat="%y-%m-%d %H:%M"):
    date = datetime.datetime.fromtimestamp(ts / 1000)
    return date.strftime(timeFormat)


def convertStrToDatetime(timeStr, timeFormat="%y-%m-%d %H:%M"):
    return datetime.datetime.strptime(timeStr, timeFormat)


def convertISOTime(isoTimeStr):
    return int(parse(isoTimeStr).timestamp() * 1000)
