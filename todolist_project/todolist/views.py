from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoModel
from .forms import TodoForm

def display_list(request):
    todoList = TodoModel.objects.all() # 데이터베이스에서 모든 ToDo 항목을 가져옴
    return render(request, 'todolist/todo_list.html', {'todoList': todoList}) # 템플릿 렌더링, todo 리스트 todo_list.html에 표시

def add_list(request): # todo 리스트 추가 함수
    if request.method == 'POST': # 요청이 POST 메소드일 때
        form = TodoForm(request.POST) # POST 메소드의 데이터로 폼 초기화
        if form.is_valid(): # 폼의 데이터가 유효할 때
            form.save() # 폼의 데이터 저장
            return redirect('display_list') # display_list로 리디렉션
    else:
        form = TodoForm() # 빈 폼을 초기화
    return render(request, 'todolist/add_list.html', {'form': form}) # 템플릿 렌더링, 폼을 add_list.html에 전달

def delete_list(request, pk): # todo 리스트 삭제 함수
    todList = get_object_or_404(TodoModel, pk=pk) # 주어진 pk에 해당하는 todo 리스트 가져옴 (없으면 404 발생)
    if request.method == 'POST': # 요청이 POST 메소드일 때
        todList.delete() # todo 리스트 삭제
        return redirect('display_list') # display_list로 리디렉션
    return render(request, 'todolist/delete_list.html', {'todList': todList}) # 템플릿 렌더링, 삭제할 todo 리스트를 delete_list.html에 전달
