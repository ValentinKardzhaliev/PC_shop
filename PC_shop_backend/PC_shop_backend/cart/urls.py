from django.urls import path

from PC_shop_backend.cart.views import add_to_cart, get_user_cart

urlpatterns = [
    path('add/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('user_cart/', get_user_cart, name='user_cart'),
]