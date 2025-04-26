from django.urls import path
from . import views

app_name = 'product_post'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='product_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='product_post'),
]