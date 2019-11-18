import json
import redis
import pymongo
from flask import Flask
from flask import request
import logging

try:
    from task2.storage import Storage
except:
    from storage import Storage

user = "user"
password = "user"
host = "172.22.0.3:27017"

app = Flask(__name__)

logging.info("Server Initiated")

redisClient = redis.Redis(host='rediska', port=6379, decode_responses=True)
logging.info("Redis Initiated")
mongoClient = pymongo.MongoClient(host='mongodb', port=27017, username="user", password="user")
logging.info("Mongo Initiated")

storage = Storage(redisClient, mongoClient['flaskdb']['cache'])


@app.route('/cache/<key>', methods=['GET'])
def get_value(key):
    value = storage.get(key)
    if value is None:
        return '', 404
    return json.loads(value)


@app.route('/cache/<key>', methods=['DELETE'])
def delete_value(key):
    storage.delete(key)
    return '', 204


@app.route('/cache/<key>', methods=['PUT'])
def add_value(key):
    if not request.is_json:
        return '', 400
    content = request.get_json()
    value = json.dumps(content)
    storage.put(key, value)
    return '', 201


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
