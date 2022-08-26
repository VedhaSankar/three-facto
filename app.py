
from unicodedata import category
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  

DB_NAME = 'trials'
database = client[DB_NAME]

app = Flask(__name__)


@app.route('/')
def start():

    return render_template('index.html')

@app.route('/home')
def home():

    return render_template('home.html')


@app.route('/categories/', methods = ['GET', 'POST'])
def categories(category):

    print(category)


    return render_template('items.html')

    # return render_template('home.html')

@app.route('/new-product', methods=['GET', 'POST'])
def new_product():

    if request.method == 'POST':
        c_name    = request.values.get("c_name")
        p_name    = request.values.get("p_name")
        price    = request.values.get("price")
        inventory    = request.values.get("inventory")
        categories    = request.values.get("categories")
        description    = request.values.get("description")


        result = {
            'Company name'  : c_name,
            'Product name'  : p_name,
            'Price'         : price,
            'inventory'     : inventory,
            'categories'    : categories,
            'description'   : description,
        }

        collection_name = 'products'

        new_collection = database[collection_name]
        x = new_collection.insert_one(result)

        print(x)

        return render_template('new_product.html', result="Inserted")

    return render_template('new_product.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)