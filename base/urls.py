from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('rooms/create/', views.createRoom, name="createRoom"),
    path('rooms/update/<str:pk>/', views.updateRoom, name="updateRoom"),
    path('rooms/delete/<str:pk>/', views.deleteRoom, name="deleteRoom"),
    path('sign-in/', views.loginPage, name="loginPage"),
    path('sign-out/', views.logoutUser, name="logoutUser"),
    path('sign-up/', views.registerUser, name="sign-up"),
]