from django.contrib import admin
from django.urls import path


from .views import *

app_name = 'core'

urlpatterns = [
    path('menu/', HomeView.as_view(), name='item_list'),
    path('', HomeView2.as_view(), name='item_list2'),
    path('2/', HomeView3.as_view(), name='item_list_2'),
    path('3/', HomeView4.as_view(), name='item_list_3'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('product2/<slug>/', ItemDetailView2.as_view(), name='product2'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('order-summary', OrderSummeryView.as_view(), name='order-summary'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('category/<str:slug>/', Post_By_Category.as_view(), name='category'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    ]