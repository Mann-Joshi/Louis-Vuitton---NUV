from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Product

class LV(TemplateView):
    template_name="homepage.html"

class construction(TemplateView):
    template_name="construction.html"

class men(ListView):
    model = Product
    template_name="men.html"
    context_object_name = "products"

class women(ListView):
    model = Product
    template_name="women.html"
    context_object_name = "products"

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm, SellerRegistrationForm, SellerLoginForm

def seller_login(request):
    if request.user.is_authenticated:
        return redirect('seller_dashboard')
        
    if request.method == 'POST':
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('seller_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = SellerLoginForm()
    return render(request, 'login.html', {'form': form})

def seller_register(request):
    if request.user.is_authenticated:
        return redirect('seller_dashboard')
        
    if request.method == 'POST':
        form = SellerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('seller_login')
    else:
        form = SellerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def seller_logout(request):
    logout(request)
    return redirect('seller_login')

@login_required(login_url='seller_login')
def seller_dashboard(request):
    return render(request, 'seller_dashboard.html')

@login_required(login_url='seller_login')
def seller_products(request):
    products = Product.objects.all()
    return render(request, 'seller_products.html', {'products': products})

@login_required(login_url='seller_login')
def seller_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller_products')
    else:
        form = ProductForm()
    return render(request, 'seller_add_product.html', {'form': form})

@login_required(login_url='seller_login')
def seller_update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'seller_update_product.html', {'form': form})
