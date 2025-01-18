from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect

from .models import Product, Category, Cart, UserType, User


def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'product': product, 'category': category})

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_type_id = request.POST['type']
        password = request.POST['password']
        user_type = UserType.objects.get(id=user_type_id)

        User.objects.create(name=name, type=user_type, password=password)
        messages.success(request, 'Registration successful!')
        return redirect('login')

    user_types = UserType.objects.all()
    return render(request, 'register.html', {'user_types': user_types})

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        try:
            user = User.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')

    return render(request, 'login.html')

def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = {}

    cart = request.session['cart']
    product = Product.objects.get(id=product_id)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': product.sale,
            'quantity': 1
        }

    request.session['cart'] = cart
    messages.success(request, 'Product added to cart!')
    return redirect('index')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})