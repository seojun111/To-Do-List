from django.contrib import admin
from django.urls import path, include

urlpatterns = [ # 프로젝트의 URL 패턴을 정의
    path('admin/', admin.site.urls), # Django의 관리자 사이트를 연결
    path('', include('todolist.urls')), # todolist 앱의 URL 패턴을 프로젝트의 루트 URL에 연결
]
