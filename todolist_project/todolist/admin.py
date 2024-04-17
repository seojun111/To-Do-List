from django.contrib import admin
from .models import TodoModel

admin.site.register(TodoModel) # 클래스를 관리자 페이지에 등록
