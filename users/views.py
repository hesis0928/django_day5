from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
# users/views.py

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todo:list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login  # ← 옵션: 가입 직후 자동 로그인

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # ① form.is_valid() 체크
        if form.is_valid():
            user = form.save()
            # (옵션) 가입 후 바로 로그인 처리
            auth_login(request, user)
            # ② 검증 통과 시 반드시 redirect 해 줄 것
            return redirect('cbv:cbv_todo_list')
        # else: 유효성 실패 → form.errors 에 메시지가 담겨 있음
    else:
        form = UserCreationForm()

    # 최종적으로 render 할 때는 항상 form 객체를 넘겨 줘야 폼과
    # 오류 메시지가 화면에 나타납니다.
    return render(request, 'registration/signup.html', { 'form': form })