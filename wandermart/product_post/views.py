from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from storefront.models import Storefront
from django.contrib.auth.models import User
from .exceptions import LoginRequired
# pagination
from django.views.generic import ListView

# le forms
from .forms import ReviewForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def product_list(request):
    products = Product.published.all()
    return render(request, 'product_post/product/list.html', {"products": products})

@login_required(login_url='product_post:loginformpage')
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
        review_form = ReviewForm(data=request.POST, request=request)


        if review_form.is_valid():
            new_review = review_form.save(commit=False)

            new_review.product = product
            new_review.user = request.user

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


# check if user logged in
def AccountLogin(request):

    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Successfully logged in as {user.username}!")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        login_form = LoginForm()
    return render(request, 'product_post/login.html', {'login_form': login_form})
    
    '''if request.method == "POST":
        login_form = LoginForm(data=request.POST)
    
    else:
        login_form = LoginForm()

    return render(request, 'product_post/login.html', {"login_form":login_form})'''


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully logged out!")
    else:
        messages.info(request, "You are already logged out.")
    return redirect("product_post:product_list")

    '''logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect(request, 'product_post/product/list.html')'''