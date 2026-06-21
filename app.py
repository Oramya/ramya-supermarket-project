
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request, redirect, session
from flask import send_file
from reportlab.pdfgen import canvas
from datetime import datetime
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = 'static/images'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "ramya"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

# USER TABLE
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100))

    password = db.Column(db.String(100))


# PURCHASE HISTORY TABLE
class Purchase(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100))

    total = db.Column(db.Integer)

    date = db.Column(db.String(100))

#PRODUCT TABLE
class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    price = db.Column(db.Integer)

    image = db.Column(db.String(100))

    category = db.Column(db.String(100)) 
# PRODUCTS
products = [

    {
        "id": 1,
        "name": "Rice",
        "price": 20,
        "image": "rice.webp",
        "category": "Grocery",
        "stock": 100
    },

    {
        "id": 2,
        "name": "Sugar",
        "price": 30,
        "image": "Sugar.webp",
        "category": "Grocery",
        "stock": 90
    },

    {
        "id": 3,
        "name": "Oil",
        "price": 80,
        "image": "Oil.webp",
        "category": "Grocery",
        "stock": 200   
    },

    {
        "id": 4,
        "name": "Chocolate",
        "price": 60,
        "image": "Chocolate.webp",
        "category": "Snacks",
        "stock": 50
    },

    {
    "id": 5,
    "name": "Milk",
    "price": 30,
    "image": "milk.webp",
    "category": "Dairy",
    "stock": 100
    },
    {
    "id": 6,
    "name": "Eggs",
    "price": 70,
    "image": "eggs.webp",
    "category": "Dairy",
    "stock": 80
    },

    {
    "id": 7,
    "name": "Bread",
    "price": 40,
    "image": "bread.webp",
    "category": "Bakery",
    "stock": 120
    },

    {
    "id": 8,
    "name": "Jam",
    "price": 60,
    "image": "jam.webp",
    "category": "Grocery",
    "stock": 90
    },

    {
    "id": 9,
    "name": "Honey",
    "price": 120,
    "image": "honey.webp",
    "category": "Grocery",
    "stock": 70
    },


    {
    "id": 10,
    "name": "Almond Seeds",
    "price": 250,
    "image": "almond_seeds.webp",
    "category": "Dry Fruits",
    "stock": 60 
    },

    {
    "id": 11,
    "name": "Cashew",
    "price": 300,
    "image": "cashew.webp",
    "category": "Dry Fruits",
    "stock": 50 
    },

    {
    "id": 12,
    "name": "Pistha",
    "price": 350,
    "image": "pistha.webp",
    "category": "Dry Fruits",
    "stock": 100    
    },

    {
    "id": 13,
    "name": "Walnuts",
    "price": 400,
    "image": "walnuts.webp",
    "category": "Dry Fruits",
    "stock": 80
    },

    {
    "id": 14,
    "name": "Cool Drinks",
    "price": 40,
    "image": "cool_drinks.webp",
    "category": "Beverages",
    "stock": 200  
    
    },
    {
    "id": 15,
    "name": "Tomato",
    "price": 25,
    "image": "tomato.webp",
    "category": "Vegetables",
    "stock": 267
    },
    {
    "id": 16,
    "name": "Brinjal",
    "price": 40,
    "image": "brinjal.webp",
    "category": "Vegetables",
    "stock": 249
    },

    {
    "id": 17,
    "name": "Cheese",
    "price": 120,
    "image": "cheese.webp",
    "category": "Dairy",
    "stock": 289
    },

    {
    "id": 18,
    "name": "Curry Leaves",
    "price": 10,
    "image": "curry_leaves.webp",
    "category": "Vegetables",
    "stock": 200  
    },

    {
    "id": 19,
    "name": "Fashion Saree",
    "price": 1500,
    "image": "fashion_saree.webp",
    "category": "Fashion",
    "stock": 200  
    },

    {
    "id": 20,
    "name": "Ice Cream",
    "price": 80,
    "image": "ice_cream.webp",
    "category": "Frozen Foods",
    "stock": 200  
    },

    {
    "id": 21,
    "name": "Biscuit",
    "price": 25,
    "image": "biscuit.webp",
    "category": "Snacks",
    "stock": 200  
    },

    {
    "id": 22,
    "name": "Chilli Powder",
    "price": 90,
    "image": "chilli_powder.webp",
    "category": "Grocery",
    "stock": 200  
    },

    {
    "id": 23,
    "name": "Cotton Sarees",
    "price": 1200,
    "image": "cotton_saress.webp",
    "category": "Fashion",
    "stock": 200  
    },

    {
    "id": 24,
    "name": "Pasta",
    "price": 90,
    "image": "pasta.webp",
    "category": "Grocery",
    "stock": 200  
    },

    {
    "id": 25,
    "name": "Pistha",
    "price": 350,
    "image": "pistha.webp",
    "category": "Dry Fruits",
    "stock": 200
    },

    {
    "id": 26,
    "name": "Designer Saree",
    "price": 1800,
    "image": "sarees.webp",
    "category": "Fashion",
    "stock": 200
    },

    {
    "id": 27,
    "name": "Spices",
    "price": 150,
    "image": "species.webp",
    "category": "Spices",
    "stock": 200
    },

    {
    "id": 28,
    "name": "Sweet",
    "price": 200,
    "image": "sweet.webp",
    "category": "Snacks",
    "stock": 267
    },

    {
    "id": 29,
    "name": "Turmeric Powder",
    "price": 80,
    "image": "turmaric_powder.webp",
    "category": "Spices",
    "stock": 267
    },

    {
    "id": 30,
    "name": "Walnuts",
    "price": 400,
    "image": "walnuts.webp",
    "category": "Dry Fruits",
    "stock": 300
    },
    {
    "id": 31,
    "name": "Apple",
    "price": 120,
    "image": "apple.webp",
    "category": "Fruits",
    "stock": 267
    },

    {
    "id": 32,
    "name": "Banana",
    "price": 60,
    "image": "banana.webp",
    "category": "Fruits",
    "stock": 267
    },

    {
    "id": 33,
    "name": "Orange",
    "price": 90,
    "image": "orange.webp",
    "category": "Fruits",
    "stock": 267
    },

    {
    "id": 34,
    "name": "Potato",
    "price": 30,
    "image": "potato.webp",
    "category": "Vegetables",
    "stock": 267
    },

    {
    "id": 35,
    "name": "Onion",
    "price": 40,
    "image": "onion.webp",
    "category": "Vegetables",
    "stock": 267
    },

    {   
    "id": 36,
    "name": "Soap",
    "price": 35,
    "image": "soap.webp",
    "category": "Personal Care",
    "stock": 267
    },
    
    ]


cart = []

@app.route('/')
def home():

    search = request.args.get('search', '')

    category = request.args.get('category', '')

    sort = request.args.get('sort', '')

    filtered_products = products

    if search:

        filtered_products = []

        for product in products:

            if search.lower() in product['name'].lower():

                filtered_products.append(product)

    if category:

        temp = []

        for product in filtered_products:

            if product['category'] == category:

                temp.append(product)

        filtered_products = temp
    if sort == "low":
         filtered_products.sort(
            key=lambda x: x['price']
        )

    elif sort == "high":
        filtered_products.sort(
            key=lambda x: x['price'],
            reverse=True
        )

    elif sort == "name":
        filtered_products.sort(
            key=lambda x: x['name']
        )    

    return render_template(
        'index.html',
        products=filtered_products
    )

    search = request.args.get('search')

    if search:

        filtered_products = []

        for product in products:

            if search.lower() in product['name'].lower():

                filtered_products.append(product)

        return render_template(
            'index.html',
            products=filtered_products
        )

    return render_template(
        'index.html',
        products=products
    )

# SIGNUP

@app.route('/signup', methods=['GET', 'POST'])

def signup():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        user = User(
            username=username,
            password=password
        )

        db.session.add(user)

        db.session.commit()

        return redirect('/login')

    return render_template('signup.html')


# LOGIN

@app.route('/login', methods=['GET', 'POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        user = User.query.filter_by(
            username=username,
            password=password
        ).first()

        if user:

            session['user'] = username

            return redirect('/dashboard')

    return render_template('login.html')



# DASHBOARD
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search', '')
    category = request.args.get('category', '')

    filtered_products = products

    # Search filter
    if search:
        filtered_products = []

        for product in products:
            if search.lower() in product['name'].lower():
                filtered_products.append(product)

    # Category filter
    if category:
        category_products = []

        for product in filtered_products:
            if product['category'] == category:
                category_products.append(product)

        filtered_products = category_products

    return render_template(
        'dashboard.html',
        products=filtered_products
    )

# ADD TO CART
@app.route('/add_to_cart/<int:id>', methods=['POST'])
def add_to_cart(id):

    quantity = int(request.form['quantity'])

    for product in products:

        if product['id'] == id:

            if quantity > product['stock']:
                return "Not enough stock available"

            product['stock'] -= quantity

            item = {
                "id": product['id'],
                "name": product['name'],
                "price": product['price'],
                "quantity": quantity,
                "subtotal": product['price'] * quantity
            }

            cart.append(item)

            break

    return redirect('/cart')
# CART PAGE
@app.route('/cart')
def cart_page():

    if 'user' not in session:
        return redirect('/login')

    total = 0

    for item in cart:
        total += item['subtotal']

    return render_template(
        'cart.html',
        cart=cart,
        total=total
    )

# ADMIN PAGE

@app.route('/admin')
def admin():

    if 'user' not in session:
        return redirect('/login')

    return render_template(
        'admin.html',
        products=products
    )
#product 

@app.route('/add_product', methods=['POST'])
def add_product():

    name = request.form['name']
    price = int(request.form['price'])
    image_file = request.files['image']

    filename = secure_filename(
        image_file.filename
    )

    image_file.save(
        os.path.join(
            app.config['UPLOAD_FOLDER'],
            filename
        )
    )
    category = request.form['category']

    new_product = {
        "id": len(products) + 1,
        "name": name,
        "price": price,
        "image": filename,
        "category": category
    }

    products.append(new_product)

    return redirect('/admin')

# delete product

@app.route('/delete_product/<int:id>')
def delete_product(id):

    for product in products:

        if product['id'] == id:
            products.remove(product)
            break

    return redirect('/admin')
# LOGOUT

@app.route('/logout')

def logout():

    session.pop('user', None)

    return redirect('/login')
@app.route('/buy_now/<int:id>', methods=['POST'])
def buy_now(id):

    if 'user' not in session:
        return redirect('/login')

    quantity = int(request.form['quantity'])

    cart.clear()

    for product in products:

        if product['id'] == id:

            if quantity > product['stock']:
                return "Not enough stock available"

            product['stock'] -= quantity

            item = {
                "id": product['id'],
                "name": product['name'],
                "price": product['price'],
                "quantity": quantity,
                "subtotal": product['price'] * quantity
            }

            cart.append(item)

            break

    return redirect('/bill')
#BILL PAGE
@app.route('/bill')
def bill():

    if 'user' not in session:
        return redirect('/login')

    total = 0

    for item in cart:
        total += item['subtotal']

    # Save purchase history
    purchase = Purchase(
        username=session['user'],
        total=total,
        date=datetime.now().strftime("%d-%m-%Y %I:%M %p")
    )

    db.session.add(purchase)
    db.session.commit()

    return render_template(
        'bill.html',
        cart=cart,
        total=total,
        username=session['user'],
        date=datetime.now()
    )
# PURCHASE HISTORY
@app.route('/history')
def history():

    if 'user' not in session:
        return redirect('/login')

    purchases = Purchase.query.filter_by(
        username=session['user']
    ).all()

    print("PURCHASES =", purchases)

    return render_template(
        'history.html',
        purchases=purchases
    )
# ANALYTICS
@app.route('/analytics')
def analytics():

    if 'user' not in session:
        return redirect('/login')

    purchases = Purchase.query.all()

    total_orders = len(purchases)

    total_revenue = 0

    customers = []

    for purchase in purchases:

        total_revenue += purchase.total

        if purchase.username not in customers:
            customers.append(purchase.username)

    total_customers = len(customers)

    if total_orders > 0:
        average_order = total_revenue / total_orders
    else:
        average_order = 0

    return render_template(
        'analytics.html',
        total_orders=total_orders,
        total_revenue=total_revenue,
        total_customers=total_customers,
        average_order=round(average_order, 2)
    )

# REMOVE ITEM FROM CART  
@app.route('/remove/<int:id>')
def remove_item(id):

    for item in cart:

        if item['id'] == id:
            cart.remove(item)
            break

    return redirect('/cart')


@app.route('/clear_cart')
def clear_cart():

    cart.clear()

    return redirect('/cart')

@app.route('/download_bill')
def download_bill():

    if 'user' not in session:
        return redirect('/login')

    total = 0

    for item in cart:
        total += item['subtotal']

    pdf_file = "bill.pdf"
    print("Creating PDF...")

    c = canvas.Canvas(pdf_file)
    print("PDF Saved")
    c.setFont("Helvetica-Bold", 18)
    c.drawString(180, 800, "Ramya Super Market")

    c.setFont("Helvetica", 12)
    c.drawString(50, 770, f"Customer: {session['user']}")
    c.drawString(50, 750, f"Date: {datetime.now()}")

    y = 700

    for item in cart:

        c.drawString(
            50,
            y,
            f"{item['name']} Qty:{item['quantity']} Price:{item['price']} Subtotal:{item['subtotal']}"
        )

        y -= 30

    c.drawString(
        50,
        y - 20,
        f"Total Amount = Rs.{total}"
    )

    c.save()   # VERY IMPORTANT

    return send_file(
        pdf_file,
        as_attachment=True
    )



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

#####if __name__ == "__main__":#
   # with app.app_context():#
       # db.create_all()#

   ####app.run(host="0.0.0.0", port=5000)#####

   