from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from mainapp.models import Member


def main(request): #메인 화면
    return render(
    request, 
    'mainapp/index.html', 
    {})

def signin(request): #로그인 화면
    return render(
    request, 
    'mainapp/signin.html', 
    {})


def signup(request):
    if request.method == "POST":
        # 비번 확인
        if request.POST["pwd"] == request.POST["pwd2"]:
            #POST 처리 코드
            real_id = request.POST.get('name')
            pw = request.POST.get('pwd')
            nick_name = request.POST.get('nick_name')
            email = request.POST.get('email')

            #DB에 저장
            creat_user = Member(
                real_id = real_id,
                pw = pw,
                nick_name = nick_name,
                email = email,)
            creat_user.save()
            return redirect('/main')

        else:
            return render(request, 'mainapp/sigup.html', {'error': 'username or password is incorrect'})
    

    return render(request, 'mainapp/signup.html')