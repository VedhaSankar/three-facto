
from unicodedata import category
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime

load_dotenv()


MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  

DB_NAME = 'trials'
database = client[DB_NAME]

app = Flask(__name__)


# @app.route('/')
# def start():

#     return render_template('index.html')

@app.route('/')
def home():

    return render_template('home2.html')

# @app.route('/signup', methods = ['GET', 'POST'])
# def signup():

#     if request.method == 'POST':

#         aitceid         = request.values.get('aitceid')
#         uname           = request.values.get('uname')
#         college_name    = request.values.get('college_name')
#         email_id        = request.values.get('email_id')
#         password        = request.values.get('password')

#         collection_name = 'user_details'

#         current_user_id = get_prev_id(collection_name) + 1

#         user_dict = {
#             '_id'           : current_user_id,
#             "aitceid"       : aitceid,
#             "uname"         : uname,
#             "college_name"  : college_name,
#             "email_id"      : email_id,
#             "password"      : password
#         }


#         new_collection = database[collection_name]
#         x = new_collection.insert_one(user_dict)
#         print(x)

#     return render_template('sign_up.html')



@app.route('/categories/', methods = ['GET', 'POST'])
def categories(category):

    print(category)


    return render_template('items.html')

    # return render_template('home.html')

@app.route('/new-product', methods=['GET', 'POST'])
def new_product():

    now = datetime.now()

    if request.method == 'POST':

        c_name      = request.values.get("c_name")
        p_name      = request.values.get("p_name")
        price       = request.values.get("price")
        inventory   = request.values.get("inventory")
        categories  = request.values.get("categories")
        man_site    = request.values.get("man_site")
        description = request.values.get("description")
        
        dt_string   = now.strftime("%d/%m/%Y %H:%M:%S")



        result = {
            'Company name'          : c_name,
            'Product name'          : p_name,
            'Price'                 : price,
            'Inventory'             : inventory,
            'Categories'            : categories,
            'Manufacturing site'    : man_site,
            'Description'           : description,
            'Time'                  : dt_string
        }

        collection_name = 'products'

        new_collection = database[collection_name]
        x = new_collection.insert_one(result)

        print(x)

        return render_template('new_product.html', result="Inserted")

    return render_template('new_product.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)