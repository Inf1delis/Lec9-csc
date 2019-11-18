import logging
from logging.config import fileConfig


class Storage:
    def __init__(self, redis_client, table):
        logipath = "loggin.conf"
        fileConfig(logipath, defaults={'logfilename': 'mylog.log'})
        self.logger = logging.getLogger()
        self.logger.debug('STORAGE LOGGER')
        self.redis_client = redis_client
        self.mongo_table = table

    def put(self, key, value):
        self.logger.debug("put for key [%s] and value [%s]", str(key), str(value))
        self.mongo_table.insert_one({'key': key, 'value': value})

    def get(self, key):
        self.logger.debug("get for key [%s]", str(key))
        if not self.redis_client.exists(key):
            self.logger.warning("no data in cache for key [%s]", str(key))
            value = self.mongo_table.find_one({'key': key})
            if value is not None:
                self.redis_client.set(key, str(value))
                self.logger.debug("get value from database [%s]", str(value['value']))
                return value['value']
            else:
                self.logger.error("no data in database for key [%s]", str(key))
                return None
        value = str(self.redis_client.get(key)).split('\'')[-2]
        self.logger.debug("get value from redis [%s]", value)
        return value

    def delete(self, key):
        self.logger.debug("delete for key [%s]", str(key))
        self.redis_client.delete(key)
        self.mongo_table.delete_many({'key': key})

