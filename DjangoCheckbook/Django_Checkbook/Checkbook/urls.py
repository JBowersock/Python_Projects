#this file was created by myself, via the Checkbook directory.

#imports;
from django.urls import path
from . import views

#creating the necessary url paths;
urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'), #primary key
    path('transaction/', views.transaction, name='transaction'),
]