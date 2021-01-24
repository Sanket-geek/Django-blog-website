from django.contrib import admin
from django.urls import path
from . import views

app_name = "App_Login"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("change_profile/", views.user_change, name='user_change'),
    path("password/",views.pass_change, name="pass_change"),
    path("change-profile-image/", views.add_pro_pic, name="add_pro_pic"),
    path("change-picture/", views.change_pro_pic, name="change_pro_pic")

]

