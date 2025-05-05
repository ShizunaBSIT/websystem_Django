from django.urls import path
from . import views

app_name = 'product_post'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='product_detail'),
    
]
