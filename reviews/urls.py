from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard_publico/', views.dashboard_publico, name='dashboard_publico'),
    path('dashboard_escritor/', views.dashboard_escritor, name='dashboard_escritor'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
]
