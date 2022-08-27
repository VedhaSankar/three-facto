from unicodedata import category
from flask import Flask, render_template, request, flash, redirect, session, url_for
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
from business import get_prev_id, display_all_products, get_per_category
# from gcp_upload import upload_blob
from werkzeug.utils import secure_filename
import security_utils
from utils import sort_company_data_by_ticker_data, get_each_ticker


load_dotenv()

app = Flask(__name__)


MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)  
SECRET_KEY = os.environ.get('SECRET_KEY')

DB_NAME = 'trials'
database = client[DB_NAME]
records = database.users

ALLOWED_EXTENSIONS  = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config["UPLOAD_FOLDER"] = "uploads/"
app.SECRET_KEY = SECRET_KEY


def allowed_file(filename):
    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():

    return render_template('home2.html')

@app.route('/signup', methods = ['GET','POST'])
def signup():

    if "email" in session:

        return redirect(url_for("home"))

    if request.method == 'POST':

        cs_id       = request.values.get('cs_id')
        uname       = request.values.get('uname')
        location    = request.values.get('location')
        email_id    = request.values.get('email_id')
        password    = request.values.get('password')
        user_type   = request.form.get('user_type')

        email_found = records.find_one({"email": email_id})

        if email_found:
            message = 'This email already exists in database'
            print(message)
            # check = True
            return render_template('sign_up.html', message=message)

        collection_name = 'users'

        current_user_id = get_prev_id(collection_name) + 1
        # current_user_id = 1

        if user_type == "user":
            u_id='u_'+str(current_user_id)
        else:
            u_id='m_'+str(current_user_id)


        user_dict = {
            '_id'           : current_user_id,
            "cs_id"         : cs_id,
            "uname"         : uname,
            "location"      : location,
            "email_id"      : email_id,
            "password"      : password,
            "user_type"     : user_type,
            "user_id"        :u_id
        }


        new_collection = database[collection_name]
        x = new_collection.insert_one(user_dict)

        print(x)

        return render_template('sign_up.html')

    return render_template('sign_up.html')


@app.route('/login',methods=['GET','POST'])
def login():

    if "email" in session:

        print("in session")

        return redirect(url_for("admin"))


    if request.method == 'POST':

        email       = request.form['email']
        password    = request.form['password']

        # print (email, password)

        email_found = records.find_one({"email_id" : email})

        # print (email_found)

        if email_found:
            # print("email found")

            email_val       = email_found['email_id']
            passwordcheck   = email_found['password']

            if passwordcheck == password:


            # if security_utils.match_password(passwordcheck, password):
                # print("correct password")
            #     session["email"] = email_val
                # print(session["email_id"])
                return redirect(url_for('home'))

            else:
                # if "email" in session:
                #     return redirect(url_for("admin"))
                message = 'Incorrect password'
                # print(message)
                return render_template('user_login.html', message = message)


    return render_template('user_login.html')


@app.route('/categories/<category>', methods = ['GET', 'POST'])
def categories(category):

    data = get_per_category(category)
    ticker_data = get_each_ticker()


    sorted_data = sort_company_data_by_ticker_data(data, ticker_data)

    return render_template('items.html', data = sorted_data)


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
            'Company_name'          : c_name,
            'Product_name'          : p_name,
            'Price'                 : price,
            'Inventory'             : inventory,
            'Categories'            : categories,
            'Manufacturing_site'    : man_site,
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
            # upload_blob(f'uploads/{filename}', f'{c_name}/{p_name}')
            return render_template('new_product2.html', result="Inserted") 

        else:
            flash('Allowed file type is .zip')
            return redirect(request.url)

    return render_template('new_product2.html')

@app.route('/view-all', methods = ['GET', 'POST'])
def view_all_products():

    list_of_products = display_all_products()

    result = {
        "result" : list_of_products
    }

    return render_template('view_all.html', products = result)


if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)