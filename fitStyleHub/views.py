from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db
import time

bp = Blueprint('main', __name__)


# FitStyleHub views

@bp.route('/')
def landing():
    cities = Category.query.order_by(Category.name).all()
    return render_template('landing.html',  cities = cities)

@bp.route('/men-list')
def menlist():
    menlist = Category.query.order_by(Category.name).all()
    return render_template('men.html', mens = menlist)

@bp.route('/women-list')
def womenlist():
    return render_template('women.html')

@bp.route('/products/<int:category_id>/')
def product(category_id):
    category = Category.query.get_or_404(category_id)
    product = category.products
    return render_template('product.html', products=product)

@bp.route('/thank-you')
def thankyou():
    return render_template('thanks.html')



# Referred to as "Basket" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    product_id = request.values.get('product_id')

    # retrieve order if there is one
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, fullname='', address='', email='', phone='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for product in order.products:
            totalprice = totalprice + product.price
    
    # are we adding an item?
    
    # product_id = request.form.get('product_id')  # Use request.form to get form data

    # ... (rest of your code)

    # are we adding an item?
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your cart'
            return redirect(url_for('main.order'))
        else:
            flash('item already in cart')
            return redirect(url_for('main.order'))

    # ... (rest of your code)

    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted')
        time.sleep(1)
    return redirect(url_for('main.landing'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.fullname = form.fullname.data
            order.address = form.address.data
            order.email = form.email.data
            order.phone = form.phone.data
            totalcost = 0
            for product in order.products:
                totalcost = totalcost + product.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Thank you for your order! ')
                return redirect(url_for('main.thankyou'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)