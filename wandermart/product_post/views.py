from django.shortcuts import render, get_object_or_404
from models import Product

# Create your views here.
def product_list(request):
    products = Product.published.all()
    return render(request, 'product_post/product/list.html', {"products": products})

def product_detail(request, year, month, day, product):
    product = get_object_or_404(Product, status='published', page=product, 
            publish__year = year,
            publish__month = month,
            publish__day = day,
            )
    
    return render(request, 'product_post/product/detail.html', {"product": product})