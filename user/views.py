from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
# Create your views here.

# login


def user_login(request):
    message = ''
    if request.method == "POST":
        if request.POST.get('register'):
            return redirect('register')  # 重新導向register網頁
        if request.POST.get('login'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == '' or password == '':
                message = '帳號跟密碼不能為空'
            else:
                user = authenticate(
                    request, username=username, password=password)

                if not user:
                    message = '帳號或密碼錯誤'
                else:
                    message = '登入成功！！'
                    login(request, user)
                    return redirect('todo')
    return render(request, './user/login.html', locals())


# register model
def user_register(request):
    message = ''
    form = CustomUserForm()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')  # 取得前端的name
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        # 密碼問題
        if password1 != password2:
            message = '兩次密碼輸入不同'
        # 密碼過短
        elif len(password1) < 8:
            message = '密碼過短(至少8個字元)'
        else:
            # 帳號重複
            if User.objects.filter(username=username).exists():
                message = 'user重複'
            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                email=email)
                if user is not None:
                    user.save()
                    print('註冊成功！！')
                    login(request, user)
                    return redirect('todo')
    return render(request, './user/register.html', locals())


@login_required
def user_profile(request):
    return render(request, './user/profile.html', locals())


@login_required
def user_logout(request):
    logout(request)

    return redirect('todo')
