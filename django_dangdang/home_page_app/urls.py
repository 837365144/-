from django.urls import path, include

from home_page_app import views

urlpatterns = [
    path('page/',include(([
        path('index/',views.home_page,name='index'),
        path('category_list/',views.book_category_list,name='category_list'),
        path("details/",views.book_details,name="details")
    ],'page'))),
]