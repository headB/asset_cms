from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.index),
    path('',views.index),
    path('verify_code/',views.verify_code),
    path("check_login/",views.check_login),
    path("register/",views.register),
    path("register/ajax",views.ajax_handle),
    path("register/register_handle",views.register_handle),
    path("index/",views.index_show),
    path("exit/",views.exit),

]