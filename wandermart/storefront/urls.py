from django.urls import path
from . import views

app_name = 'storefront'

urlpatterns = [
    path('', views.store_list, name='store_list'),
    #path('<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='product_detail'),
    path('<slug:store_slug>/', views.store_page, name='store_page'),
]
