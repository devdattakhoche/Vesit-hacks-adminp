from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('submitted/', views.submit, name='submit'),
    path('adminp/', views.adminp, name='adminp'),
]