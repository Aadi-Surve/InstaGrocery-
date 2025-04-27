from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    prod = Product.objects.all()
    fm = ProductForm()
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if fm.is_valid():
            fm.save()
            return redirect("success")  # Make sure "sucess" URL name exists!
    else:
        fm = ProductForm()  # GET request → show empty form

    return render(request, 'InstaGrocery/home.html', {'prod': prod, 'fm': fm})

def edit_product(request, product_id):
    prod = Product.objects.get(id=product_id)
    if request.method == "POST" :
        fm = ProductForm(request.POST, request.FILES, instance=prod)
        if fm.is_valid():
            fm.save()
            return redirect("home")  # Make sure "sucess" URL name exists!
    else:
        fm = ProductForm(instance=prod)  # GET request → show existing product

    return render(request, 'InstaGrocery/edit_product.html', {'fm': fm})

def delete_product(request, product_id):
    prod = Product.objects.get(id=product_id)
    if request.method == "POST":
        prod.delete()
        return redirect("home")  # Make sure "sucess" URL name exists!
    return render(request, 'InstaGrocery/delete_product.html', {'prod': prod})

def success(request):
    return render(request, 'InstaGrocery/success.html')