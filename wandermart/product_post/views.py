from django.shortcuts import render, get_object_or_404
from .models import Product, Review
from storefront.models import Storefront
# pagination
from django.views.generic import ListView

# le forms
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_list(request):
    products = Product.published.all()
    return render(request, 'product_post/product/list.html', {"products": products})

def product_detail(request, year, month, day, product):
    product = get_object_or_404(Product, slug=product, status='published', 
            publish__year = year,
            publish__month = month,
            publish__day = day
            )
    
    #reviews
    reviews = product.reviews.filter(active=True)
    new_review = None
    
    if request.method == "POST":
        #review_form = ReviewForm(data=request.POST, user=request.user)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            new_review = review_form.save(commit=False)

            new_review.product = product

            new_review.save()
    
    else:
        #review_form = ReviewForm(user=request.user)
        review_form = ReviewForm()


    return render(request, 'product_post/product/detail.html', {"product": product, 'reviews': reviews, 'new_review':new_review, 'review_form': review_form})

class ProductListView(ListView):
    queryset = Product.published.all()
    context_object_name = "products"
    paginate_by = 10
    template_name = "product_post/product/list.html"

