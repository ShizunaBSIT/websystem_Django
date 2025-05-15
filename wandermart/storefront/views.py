from django.shortcuts import render, get_object_or_404
from .models import Storefront

# Create your views here.
def store_list(request):
    stores = Storefront.objects.all()

    return render(request, "storefront/storefront/list.html")

def store_page(request, store):
    store = get_object_or_404(store, slug=store,)

    return render(request,"storefront/storefront/store.html",{'store':store})