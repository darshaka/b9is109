from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('register/', views.userRegister, name="register"),
    path('', views.home, name="home"),
    path('newspaper/<str:pk>/', views.newspaper, name="newspaper"),
    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('update-user/', views.update_user, name="update-user"),

    path('create-newspaper', views.newspaper_create, name="create-newspaper"),
    path('update-newspaper/<str:pk>/', views.newspaper_update, name="update-newspaper"),
    path('delete-newspaper/<str:pk>/', views.newspaper_delete, name="delete-newspaper"),
]