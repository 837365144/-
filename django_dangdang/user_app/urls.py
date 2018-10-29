from django.urls import path, include

from user_app import views

urlpatterns = [
    path('register/',include(([
        path('page/',views.register_page,name='page'),
        path('logic/',views.register_logic,name='logic'),
        # path('ok/',views.register_ok,name="ok"),
        path("yzm_ajax/",views.ajax_captcha,name="yzm_ajax"),
        path("username_ajax/",views.ajax_username,name="username_ajax"),
    ],'register'))),
    path('captcha/',include(([
        path('show/',views.get_captcha,name='show'),
    ],'captcha'))),
    path('login/',include(([
        path('page/',views.login_page,name='page'),
        path("login_logic_ajax/",views.ajax_login_logic,name="login_logic_ajax")
    ],'login'))),
]