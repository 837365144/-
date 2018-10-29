from django.urls import path, include

from order_app import views

urlpatterns = [
    path('index/',include(([
        path('page/',views.order_page,name='page'),
        path('modify/',views.modify_Cart_2,name='modify'),
    ],'index'))),
    path('close/',include(([
        path('address/',views.address_logic,name='address'),
        # path('ok/',views.order_ok,name='ok')
    ],'close'))),
]