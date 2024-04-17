from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_list, name='display_list'), # 뷰 함수 todo_list 연결
    path('add/', views.add_list, name='add_list'), # 뷰 함수 add_list 연결
    path('delete/<int:pk>/', views.delete_list, name='delete_list') # 뷰 함수 delete_list 연결
]
