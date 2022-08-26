
from unicodedata import category
from flask import Flask, render_template, request, flash, redirect, session
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from gcp_upload import upload_blob
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)

MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_EXTENSIONS  = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config["UPLOAD_FOLDER"] = "uploads/"
app.SECRET_KEY = SECRET_KEY


DB_NAME = 'trials'
database = client[DB_NAME]

def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():

    return render_template('home2.html')

@app.route('/categories/<category>', methods = ['GET', 'POST'])
def categories(category):

    print(category)


    return render_template('items.html')


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

        if 'file' not in request.files:

            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':

            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            upload_blob(f'uploads/{filename}', f'product_{c_name}_{p_name}/{filename}')
            return render_template('new_product2.html', result="Inserted") 

        else:
            flash('Allowed file type is .zip')
            return redirect(request.url)

    return render_template('new_product2.html')


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)