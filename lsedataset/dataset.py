import redis




class DataSet (object):
    def __init__(self):
        self.redis_host = "Redis"
        self.redis_port = 6379
        self.redis_password = ""

    def hello(self):
        try:
            r = redis.StrictRedis(host=self.redis_host, port=self.redis_port, password=self.redis_password, decode_responses=True)
            r.set("msg:hello", "Hello Redis!!!")
            msg = r.get("msg:hello")
            print(msg)
        except Exception as e:
            print(e)

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
