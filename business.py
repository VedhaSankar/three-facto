import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os
from gcp_image import list_blobs

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

client = MongoClient(MONGO_URI)
DB_NAME = 'trials'
database = client[DB_NAME]

BUCKET_NAME = os.environ.get('BUCKET_NAME')


def get_prev_id(db):

    collection = database[db]
    last_id = collection.find().sort([("_id", pymongo.DESCENDING)]).limit(1)

    for i in last_id:
        return i['_id']


def display_all_products():

    list_of_products = []

    collection = database['products']
    products = collection.find()

    image_url_list = get_image_url_list()

    print(image_url_list)

    for product in products:

        product_str = [product['Company_name'], product['Product_name']]
        
        print(product_str)
        
        for item in image_url_list:
            
            print (item)
            
            if product_str[0] and product_str[1] in item:
                
                product['image_url'] = item
                break
                
        list_of_products.append(product)

    print (list_of_products)

    return list_of_products


def get_image_url_list():

    blobs_list = list_blobs(BUCKET_NAME)

    image_url_list = []

    for item in blobs_list:

        x = item.replace(" ", "%20")

        final = 'https://storage.googleapis.com/trifacto/' + x

        # print(final)

        image_url_list.append(final)

    return image_url_list

def get_per_category(category):

    database = client['trials']
    col = database.products

    res = []

    for x in col.find({"Categories":category}):

        del x["_id"]

        res.append(x)
    
    return res


def main():

    # print(get_prev_id('trials'))
    display_all_products()
    # get_image_url_list()


if __name__ == '__main__':  
    main()