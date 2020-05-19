from django.urls import path
from userapp import views
urlpatterns = [
    path('', views.index, name="homepage"),
    path('login/', views.loginview, name="login"),
    path('logout/', views.logoutview, name="logout"),
    path('signup/', views.signupview, name="signup")
]