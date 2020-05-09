import redis




class DataSet (object):
    def __init__(self):
        self.redis_host = "Redis"
        self.redis_port = 6379
        self.redis_password = ""

    def insert(self, name, value):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            r.set(name, value)
        except Exception as e:
            print(e)

    def getValue(self, name):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            msg = r.get(name)
            print(msg)
        except Exception as e:
            print(e)

    def insertVideo(self, wordsList):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            for item in wordsList:
                print("Adding " + item['word'] + "...")
                r.hmset(item['word'],item)
        except Exception as e:
            print(e)

    def getWord(self, search):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            item = r.hgetall(search)
            print(item)
        except Exception as e:
            print(e)

    def listWords(self):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            item = r.keys('*')
            print(item)
        except Exception as e:
            print(e)

    def deleteWord(self, search):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            item = r.delete(search)
            print("Removing " + search + "...")
        except Exception as e:
            print(e)
