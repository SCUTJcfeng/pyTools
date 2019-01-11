#!/usr/bin/python3
# -*- coding:utf-8 –*-

import csv


def writeCSVData(fileName, headers, dataList):
    with open(fileName, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in dataList:
            writer.writerow(row)


def readCSVData(fileName):
    dataList = []
    with open(fileName, 'r', newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            dataList.append(dict(row))
    return dataList


if __name__ == "__main__":
    dataList = [
        {'a': 'a1', 'b': 'a1', 'c': 'a1'},
        {'a': 'a2', 'b': 'a2', 'c': 'a2'},
        {'a': 'a3', 'b': 'a3', 'c': 'a3'},
    ]
    headers = ['a', 'b', 'c']

    writeCSVData('temp.csv', headers, dataList)

    print(readCSVData('temp.csv'))
