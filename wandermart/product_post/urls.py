from django.urls import path
from . import views

app_name = 'product_post'

urlpatterns = [
    path('', views.product_list, name='list'),  
    path('products/', views.product_list, name='list'),  
    path('products/<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='detail'),
]
