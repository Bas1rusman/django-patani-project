from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListCreate.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('persons/', views.PersonListCreate.as_view(), name='person-list'),  
    path('persons/<int:pk>/', views.PersonDetail.as_view(), name='person-detail'),
    path('proyek/', views.ProyekListCreate.as_view(), name='proyek-list'),  
    path('proyek/<int:pk>/', views.ProyekDetail.as_view(), name='proyek-detail'),
    path('petani/', views.PetaniListCreate.as_view(), name='petani-list'),  
    path('petani/<int:pk>/', views.PetaniDetail.as_view(), name='petani-detail'),
]
