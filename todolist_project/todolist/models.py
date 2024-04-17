from django.db import models

class TodoModel(models.Model): # 모델 정의
    title = models.CharField(max_length=50) # todo 리스트의 제목 저장
    completed = models.BooleanField(default=False) # todo 리스트의 완료 여부

    def __str__(self): # todo 리스트의 제목을 문자열로 반환
        return self.title
