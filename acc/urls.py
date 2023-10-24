from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterApiView.as_view()),
    path('LoginApi/', views.LoginApiView.as_view()),
    path('me/', views.UserApiView.as_view()),
    path('gettoken/', views.TokenApiView.as_view()),
    path('Logout/', views.LogOutView.as_view())
]