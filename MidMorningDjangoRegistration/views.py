from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import SupplierRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required()
def add_product(request):
    # Check if the form submitted has a method post
    if request.method == "POST":
        # Start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST.get('bei')

        # Finally save the data in our table called products
        product = Product(prod_name=p_name, prod_quantity=p_quantity, prod_price=p_price)
        product.save()
        # Redirect back with a success message
        messages.success(request, 'Product saved successfully')
        return redirect('add-product')
    return render(request, 'add-product.html')


@login_required()
def view_products(request):
    # Select all the products to be displayed
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def view_supplier(request):
    if request.method == 'POST':
        form = SupplierRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier added successfully')
        return redirect('supplier')
    else:
        form = SupplierRegistrationForm()
    return render(request, 'supplier.html', {'form': form})
