from django import forms # Django의 forms 모듈을 가져옵니다.
from .models import TodoModel # TodoModel 모델을 가져옵니다.
 
class TodoForm(forms.ModelForm): # ModelForm 클래스를 상속
    class Meta: # 폼에 대한 추가적인 정보
        model = TodoModel # 폼이 사용할 모델 지정
        fields = ['title'] # todo 리스트를 입력 받을 때 title 필드만 허용
