# blog/views.py
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

async def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

def add_product(request):
    # Logic to add product (assuming this is implemented)
    return redirect('product_list')  # Redirects to the product list after adding a product

from django.views.decorators.http import require_GET
from django.shortcuts import render


@require_GET  # Only allows GET requests
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

from django.views.decorators.http import require_POST

@require_POST  # Only allows POST requests
def add_product(request):
    # Logic to add a product
    return redirect('product_list')

from django.views.decorators.gzip import gzip_page

@gzip_page  # Compresses the response if the client supports gzip
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

from django.views.decorators.cache import never_cache

@never_cache  # Ensures the response is never cached
def add_product(request):
    # Logic to add a product
    return redirect('product_list')

from django.views.decorators.http import etag

def product_etag(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return str(product.pk)  # Generate a simple ETag using the product's primary key

@etag(product_etag)  # Sets the ETag header
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})
