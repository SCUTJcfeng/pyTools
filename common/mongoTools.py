#!/usr/bin/python3
# -*- coding:utf-8 –*-

import time
from pymongo.errors import AutoReconnect
from pymongo import MongoClient


MAX_AUTO_RECONNECT_ATTEMPTS = 5


class MongoClienBuilder(object):
    def __init__(self, host, port, db, collection, username, pwd):
        self._conn = MongoProxy(host, port, db, collection, username, pwd)

    def __getattr__(self, attr):
        if hasattr(self._conn, attr):
            def wrapper(*args, **kwargs):
                for attempt in range(MAX_AUTO_RECONNECT_ATTEMPTS):
                    try:
                        return getattr(self._conn, attr)(*args, **kwargs)
                    except AutoReconnect as e:
                        waitTs = 0.5 * pow(2, attempt)
                        print(f'PyMongo atuo-reconnecting...{e}. Waiting {waitTs} seconds.')
                        time.sleep(waitTs)
                raise AutoReconnect
            return wrapper
        raise AttributeError(attr)


class MongoProxy(object):
    def __init__(self, host, port, db, collection, username, pwd):
        self._collection = collection
        self._mongoClient = MongoClient(host=host, port=int(port), connect=False)
        self._db = self._mongoClient[db]
        self._db.authenticate(username, pwd)
        self._client = self._db[collection]

    def __del__(self):
        self._mongoClient.close()

    def counts(self):
        return self._client.count()

    def _collections(self):
        return self._db.collection_names()

    def hasCollection(self, collection):
        return collection in self._collections()

    def changeCollection(self, collection):
        self._client = self._db[collection]

    def initCollection(self):
        self._client = self._db[self._collection]

    def findOne(self, data):
        return self._client.find_one(data)

    def findOneWithoutID(self, data):
        return self._client.find_one(data, {'_id': False})

    def insertOne(self, data):
        if self.findOne(data) is None:
            self._client.insert_one(data)
            return True
        return False

    def insertMany(self, data):
        if isinstance(data, list):
            res = self._client.insert_many(data)
            return res.acknowledged

    def updateOne(self, oldData, newData, upsert=False):
        res = self._client.update_one(oldData, {'$set': newData}, upsert=upsert)
        return res.acknowledged

    def deleteOne(self, data):
        res = self._client.delete_one(data)
        return True if res.deleted.count == 1 else False

    def getAllData(self, sort=None):
        dataList = []
        if self.counts() > 0:
            res = self._client.find(projection={'_id': False}, sort=sort)
            dataList = [item for item in res]
        return {'data': dataList, 'count': len(dataList)}

    def findDataWithParams(self, params=None, skip=0, limit=0, sort=None, projection={'_id': False}):
        res = self._client.find(filter=params, projection=projection, sort=sort, skip=skip, limit=limit)
        dataList = [item for item in res]
        return {'data': dataList, 'count': len(dataList)}

    def findDataWithRange(self, field, start, end, sort=None):
        res = self._client.find(filter={field: {'$gte': start, '$lt': end}}, projection={'_id': False}, sort=sort)
        dataList = [item for item in res]
        return {'data': dataList, 'count': len(dataList)}

    def dropCollection(self):
        return self._client.drop()

    def createIndex(self, collection, index, unique=True):
        self.changeCollection(collection)
        self._client.create_index([(index, -1)], unique=unique, background=True)
