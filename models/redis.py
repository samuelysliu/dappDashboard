import redis
import json

class redisObject:
    def __init__(self):
        self.r = redis.Redis(host='redis-13140.c302.asia-northeast1-1.gce.cloud.redislabs.com', port=13140,
                        password='a7eB3gdHHr8BdPBCOjaa7d9RBxj2Fa2b')

    def saveDict(self, key, value, expired):
        #key 鍵值-字串 value 儲存的值 dict expired 幾秒後過期 int
        self.r.hmset(key, value)
        self.r.expire(key, expired)

    def getDict(self, key):
        return self.r.hgetall(key)

    def saveObject(self, key, value, expired):
        # key 鍵值-字串 value 儲存的值 dict expired 幾秒後過期 int
        self.r.set(key, json.dumps(value))
        self.r.expire(key, expired)

    def getObject(self, key):
        if self.r.get(key) == None:
            return None
        else:
            return json.loads(self.r.get(key).decode('utf-8'))

