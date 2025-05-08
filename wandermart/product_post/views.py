from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product
from django.template import engines

print(engines['django'].dirs)

def base(request):
    return render(request, 'base.html')

def product_list(request):
    # Filter products by publish date and status
    products = Product.objects.filter(status='published', publish__lte=timezone.now())  # Use `publish` instead of `published`
    return render(request, 'product_post/product/list.html', {"products": products})

def product_detail(request, year, month, day, product):
    # Fetch product details based on publish date and page slug
    product = get_object_or_404(Product, status='published', slugpage=product,
            publish__year=year,
            publish__month=month,
            publish__day=day,
            )
    
    return render(request, 'product_post/product/detail.html', {"product": product})
