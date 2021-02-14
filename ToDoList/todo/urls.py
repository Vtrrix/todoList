from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_list),
    path('add_task/', views.add_task),
    path('delete_task/', views.del_task)
]
