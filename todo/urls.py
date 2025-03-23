from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add/', views.add, name='add'),   
    path('mark_completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('mark_uncompleted/<int:pk>/', views.mark_uncompleted, name='mark_uncompleted'),
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('delet_completde/<int:pk>/',views.deleted_completed,name='delete_completed'),
        
]
