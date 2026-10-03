from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tasks/new/", views.task_create, name="task-create"),
    path("tasks/<int:pk>/edit/", views.task_edit, name="task-edit"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),
    path("signup/", views.signup, name="signup"),
]
