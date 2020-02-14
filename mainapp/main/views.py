from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from mainapp.models import Member
from django.utils import timezone
from mainapp.forms import LoginForm


def main(request): #메인 화면
    return render(
    request, 
    'mainapp/index.html', 
    {})

def signup(request):
    if request.method == "POST":
        # 비번 확인
        if request.POST["user_pw"] == request.POST["user_pw2"]:
            #POST 처리 코드
            user_id = request.POST.get('user_id')
            user_pw = request.POST.get('user_pw')
            nick_name = request.POST.get('nick_name')
            email = request.POST.get('email')
            #pi = request.POST.get('pi')

            #DB에 저장
            creat_user = Member(
                user_id = user_id,
                user_pw = user_pw,
                nick_name = nick_name,
                email = email,)
            creat_user.save()
            return redirect('/main')

        else:
            return render(request, 'mainapp/sigup.html', {'error': 'username or password is incorrect'})
    

    return render(request, 'mainapp/signup.html')


# def signin(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'mainapp/signin.html', {'form':form})
#     else:
#         user_id = request.POST['user_id']
#         user_pw = request.POST['user_pw']
#         # member = Member.objects.get(user_id=user_id, user_pw=user_pw)
#         try:
#             Member.objects.get(user_id=user_id, user_pw=user_pw)
#             # request.session['user_id'] = member.user_id
#             # request.session['member_id'] = member.member_id
           

#         except Member.DoesNotExist:
#             return HttpResponse('로그인 실패')
#             # return redirect('/main/signin')
#         else:
#             return redirect('/swipe')


def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'mainapp/signin.html', {'form':form})
    else:
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        member = Member.objects.get(user_id=user_id, user_pw=user_pw)
        request.session['user_id'] = member.user_id
        request.session['member_id'] = member.member_id

        try:
            if member:
                return redirect('/swipe/')
                
        except Member.DoesNotExist:
            return redirect('/main/signin/')
  
