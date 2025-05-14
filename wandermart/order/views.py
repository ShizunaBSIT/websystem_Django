from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from product_post.models import Product

# Create your views here.
'''def order_list(request):
    orders = Order.objects.all()

    return render(request, 'order/order/list.html', {"orders":orders})
'''

### show orders related to the currently logged in user
def order_list(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)

        return render(request, 'order/order/list.html', {'orders':orders})
    else:
        return redirect('product_post:loginformpage')


### show order detail
'''def order_detail(request, order):
    order = get_object_or_404(Order, slug=order)

    return render(request, 'order/order/order.html', {"order":order})'''

def order_detail(request, order):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, slug=order)
        return render(request, 'order/order/detail.html', {"order":order})
    else:
        return redirect('product_post:loginformpage')
    
### placing an order
@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.product = product
            order.save()

            messages.success(request, f"Order placed")
            return redirect('order:order_list')
        else:
            messages.error(request, "There was an error with processing your order.")
    else:
        order_form = OrderForm()

        return render(request, 'order/placeOrder.html', {'product': product, 'order_form':order_form})


    