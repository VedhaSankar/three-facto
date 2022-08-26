import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)
DB_NAME = 'trials'
database = client[DB_NAME]


def get_prev_id(db):

    collection = database[db]
    last_id = collection.find().sort([("_id", pymongo.DESCENDING)]).limit(1)

    for i in last_id:
        return i['_id']

        
def main():

    print(get_prev_id('trials'))


if __name__ == '__main__':  
    main()