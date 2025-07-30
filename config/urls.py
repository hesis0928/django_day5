"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from users.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),  # 회원가입·로그인·로그아웃
    path('', include('todo.urls')),            # To-Do 앱을 루트로
]
    path('accounts/signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cbv/', include(('todo.urls', 'todo'), namespace='cbv')),

    # ← 이 부분을 추가
    path('accounts/', include('django.contrib.auth.urls')),

    # Optional: 루트에 바로 리다이렉트 걸어주고 싶다면
    path('', RedirectView.as_view(pattern_name='cbv:cbv_todo_list', permanent=False)),
]



