from django.shortcuts import render, get_object_or_404
from .models import Order

# Create your views here.
def order_list(request):
    orders = Order.objects.all()

    return render(request, 'order/order/list.html', {"orders":orders})


def order_detail(request, order):
    order = get_object_or_404(Order, slug=order)

    return render(request, 'order/order/order.html', {"order":order})