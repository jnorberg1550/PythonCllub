from django.urls import path
from .import views 

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('getTypes/', views.getTypes, name = 'types'),
    path ('getResources/', views.getResources, name='resources'),
    path ('resourceDetail/<int:id>', views.resourceDetail, name ='resourceDetail'),
]