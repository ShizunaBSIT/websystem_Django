from django.urls import path
from . import views

app_name = 'product_post'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:year>/<int:month>/<int:day>/<page:product>/', views.product_detail, name='post_detail'),
    
]
