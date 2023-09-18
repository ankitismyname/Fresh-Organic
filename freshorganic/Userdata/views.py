from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')  # Redirect to the login page after successful signup
        except Exception as e:
            messages.error(request, str(e))
            return redirect('signup')

    return render(request, 'signup.html')


from .models import UserProfile

@login_required
def editprofile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        # Process the form data when the user submits the form
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.mobile_number = request.POST['mobile_number']
        profile.address = request.POST['address']

        # Update User model fields
        user.username = request.POST['username']
        user.email = request.POST['email']
        # You should use Django's built-in methods to set the password securely.
        # For example, you can use user.set_password('new_password') to set a new password.
        # Remember to import User model from django.contrib.auth.models.

        user.save()
        profile.save()
        return redirect('personal')  # Redirect to the user profile page after saving

    return render(request, 'editprofile.html', {'profile': profile})


@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # Validate the old password
        if not request.user.check_password(old_password):
            messages.error(request, 'Incorrect old password.')
            return redirect('change_password')

        # Validate the new password
        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return redirect('change_password')

        # Change the password
        request.user.set_password(new_password1)
        request.user.save()

        messages.success(request, 'Password changed successfully.')
        return redirect('home')

    return render(request, 'changepswd.html')


def home(request):
        return render(request, "main.html")

def personal(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        # Process the form data when the user submits the form
        profile.first_name = request.POST['first_name']
        profile.last_name = request.POST['last_name']
        profile.mobile_number = request.POST['mobile_number']
        profile.address = request.POST['address']

        # Update User model fields
        user.username = request.POST['username']
        user.email = request.POST['email']
        # You should use Django's built-in methods to set the password securely.
        # For example, you can use user.set_password('new_password') to set a new password.
        # Remember to import User model from django.contrib.auth.models.

        user.save()
        profile.save()
        return redirect('personal')  # Redirect to the user profile page after saving

    return render(request, 'personal.html', {'profile': profile})



def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def vegetables(request):
    return render(request,"vegetable.html")

def dryfurits(request):
    return render(request,"dryfurits.html")

def furits(request):
    return render(request,"furits.html")

def flowers(request):
    return render(request,"flowers.html")




def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the user profile page after successful login
        else:
            # If authentication fails, show an error message on the login page
            context = {'error': 'Invalid credentials. Please try again.'}
            return render(request, 'login.html', context)

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

from usercart.models import Product, ShoppingCartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item, created = ShoppingCartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('product_list')

from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
def view_cart(request):
    cart_items = ShoppingCartItem.objects.filter(user=request.user)
    subtotal = 0
    for item in cart_items:
        item_price = Decimal(str(item.product.price))
        item_quantity = Decimal(str(item.quantity))
        item_subtotal = item_price * item_quantity
        item.subtotal = item_subtotal  # Add subtotal to each cart item
        subtotal += item.product.price * item.quantity

    shipping = Decimal('5.00')  # Assuming a flat shipping rate of $5.00
    total = subtotal + shipping

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'total': total,
             }
  
    return render(request, 'view_cart.html', context)

def update_quantity(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id, user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')
        quantity = int(request.POST.get('quantity', 1))

        if action == 'decrease':
            cart_item.quantity = max(cart_item.quantity - 1, 1)
        elif action == 'increase':
            cart_item.quantity += 1

        cart_item.save()

    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(ShoppingCartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('view_cart')







