from django.urls import path
from webapp.views import ProductList, ProductView, ProductCreate, ProductUpdate, ProductDelete, ReviewList, ReviewView, ReviewCreate, ReviewUpdate, ReviewDelete

app_name = 'webapp'

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('<int:pk>/', ProductView.as_view(), name='product_view'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('reviews/', ReviewList.as_view(), name='review_index'),
    path('reviews/create/<int:pk>/', ReviewCreate.as_view(), name='review_create'),
    path('reviews/<int:pk>/', ReviewView.as_view(), name='review_view'),
    path('reviews/<int:pk>/update/', ReviewUpdate.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDelete.as_view(), name='review_delete'),
]