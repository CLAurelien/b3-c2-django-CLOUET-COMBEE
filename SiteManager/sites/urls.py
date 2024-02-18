from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('add/', views.add_site, name='add'),
    path('edit/<int:id>', views.edit_site, name='edit')
]