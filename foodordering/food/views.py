from django.shortcuts import render, redirect
from .models import food
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    foods = food.objects.all()
    return render(request, 'food/home.html', {'foods': foods})


def add_to_cart(request, food_id):
    cart = request.session.get('cart', {})

    food_item = food.objects.get(id=food_id)

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id] += 1
    else:
        cart[food_id] = 1

    request.session['cart'] = cart

    return redirect('home')
def cart(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for food_id, quantity in cart.items():
        item = food.objects.get(id=food_id)
        subtotal = item.price * quantity
        total += subtotal

        cart_items.append({
            'food': item,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'food/cart.html', {
        'cart_items': cart_items,
        'total': total
    })
def increase_cart(request, food_id):
    cart = request.session.get('cart', {})

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id] += 1

    request.session['cart'] = cart

    return redirect('cart')


def decrease_cart(request, food_id):
    cart = request.session.get('cart', {})

    food_id = str(food_id)

    if food_id in cart:
        cart[food_id] -= 1

        if cart[food_id] <= 0:
            del cart[food_id]

    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, food_id):
    cart = request.session.get('cart', {})

    food_id = str(food_id)

    if food_id in cart:
        del cart[food_id]

    request.session['cart'] = cart

    return redirect('cart')
from django.shortcuts import render, redirect
from .models import food, Order, OrderItem

def place_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart')  # nothing to order

    if request.method == 'POST':
        name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        total = 0
        items_to_save = []
        for food_id, quantity in cart.items():
            item = food.objects.get(id=food_id)
            subtotal = item.price * quantity
            total += subtotal
            items_to_save.append((item, quantity, subtotal))

        order = Order.objects.create(
            customer_name=name,
            phone=phone,
            address=address,
            total_amount=total
        )

        for item, quantity, subtotal in items_to_save:
            OrderItem.objects.create(order=order, food=item, quantity=quantity, subtotal=subtotal)

        request.session['cart'] = {}  # clear cart
        return render(request, 'food/order_success.html', {'order': order})

    return render(request, 'food/checkout.html', {'cart': cart})
def menu(request):
    foods = food.objects.all()
    return render(request, 'food/menu.html', {'foods': foods})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'food/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            login(request, user)
            return redirect('home')

    return render(request, 'food/register.html')