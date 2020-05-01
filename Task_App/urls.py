from django.urls import path
from Task_App import views

urlpatterns = [
    path('', views.taskapp, name='task'),
    path('delete/<task_id>', views.delete_task, name='delete'),
    path('edit/<task_id>', views.edit_task, name='edit'),
    path('complete/<task_id>', views.complete_task, name='complete'),
    path('pending/<task_id>', views.pending_task, name='pending'),
]
