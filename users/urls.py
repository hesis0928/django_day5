# users/urls.py
from django.urls import path
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)           # 가입 직후 자동 로그인
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

urlpatterns = [
    path('signup/',   sign_up,    name='signup'),
    path('login/',    login_view, name='login'),
    path('logout/',   redirect,   {'url': '/'}, name='logout'),
    # 또는 장고 내장 로그아웃 뷰 사용:
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
