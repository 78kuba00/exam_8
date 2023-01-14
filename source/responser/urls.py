from django.contrib import admin
from django.urls import path
from webapp.views import ProductList, ProductView, ProductCreate, ProductUpdate, ProductDelete

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('<int:pk>/', ProductView.as_view(), name='product_view'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
]