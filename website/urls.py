from django.urls import path
from .views import RegisterView, LoginView, LogoutView, product_list, product_detail, product_create, product_update, \
    product_delete

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('products/', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/create/', product_create, name='product_create'),
    path('product/update/<int:pk>/', product_update, name='product_update'),
    path('product/delete/<int:pk>/', product_delete, name='product_delete'),
]