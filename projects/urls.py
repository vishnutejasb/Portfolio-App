from django.urls import path
from projects import views

urlpatterns = [
    path('',views.testing,name='testing'),
    path("projects/", views.project_index, name="project_index"),
    path("projects/details/<int:pk>", views.project_detail, name="project_detail"),
]