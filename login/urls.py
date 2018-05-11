from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.login_index),
    path('',views.forward_to_estimate),
    path('verify_code/',views.verify_code),
    path("check_login/",views.check_login),
    path("register/",views.register),
    path("register/ajax",views.ajax_handle),
    path("register/register_handle",views.register_handle),
    path("index/",views.index),
    path("exit/",views.exit),
    path("index/ajax_estimate/",views.ajax_estimate),
    path("index/forwarder.php",views.estimate_process),

]