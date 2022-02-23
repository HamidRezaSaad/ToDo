from django.urls import  path
from . import views

app_name="users"
urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path("login/", views.login_request, name="login"),
    path("logout/",views.logout_request,name="logout"),
]