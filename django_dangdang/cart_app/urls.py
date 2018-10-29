from django.urls import path, include

from cart_app import views

urlpatterns = [
    path('cart/',include(([
        path('index/',views.shopping_cart,name='index'),
        path('add_cart/',views.addBookToCart,name="add_cart"),
        path("modify_cart/",views.modify_Cart,name="modify_cart")
    ],'cart'))),
]