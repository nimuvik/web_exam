from django.urls import path
from . import views

urlpatterns = [
    path('mvexam/', views.exam_list, name='exam_list.html'),
]
