from django.urls import path,include
from django.contrib.auth import views as auth_view
from . views import *


urlpatterns = [
    path('register/',register,name = "RegisterUrl"),
    path('login/',auth_view.LoginView.as_view(template_name = "users/login.html"), name = "LoginUrl"),
    path('logout',auth_view.LogoutView.as_view(template_name = "users/logout.html"),name = "LogoutUrl"),
    path('User/Profile',userProfileTempate, name = "userProfiileUrl"),
    path('User/<str:userid>/Profile/',AnotherUserProfile,name="AhotherUserProfile")
]
