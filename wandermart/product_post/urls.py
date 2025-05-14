from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 

app_name = 'product_post'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:product>/', views.product_detail, name='product_detail'),
    path('login/', views.AccountLogin, name='loginformpage'),
    path('logout/', views.logout_view, name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]
