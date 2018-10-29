from django.urls import path, include

from commodity_management_app import views

urlpatterns = [
    path('index/',include(([
        path('page/',views.index_page,name='page'),
    ],'index'))),
    path('add/',include(([
        path('page/',views.add_page,name='page'),
        path('ajax/',views.add_ajax,name='ajax'),
    ],'add'))),
    path('list/', include(([
      path('page/', views.list_page, name='page'),
    ], 'list'))),
    path('category_1/', include(([
      path('page/', views.category_1, name='page'),
      path('ajax/',views.category_1_ajax,name='ajax')
     ], 'category_1'))),
    path('category_2/', include(([
      path('page/', views.category_2, name='page'),
      path('ajax/',views.category_2_ajax,name='ajax')
     ], 'category_2'))),
    path('category_list/', include(([
      path('page/', views.category_list, name='page'),
     ], 'category_list'))),
]