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

        
        if member:
            return redirect('/swipe/')
            # return render(request, 'mainapp/swipe.html')
        else:
            return redirect('/main')
   

  

#   # 두번째 시도
# def signin(request):
#     if request.method == "GET":
#         return render(request, 'mainapp/signin.html')
#         # 잘못된 접근입니다. 알림뜨게 하기
    
#     elif request.method == "POST":
#         # 전송받은 아이디, 비밀번호 확인
#         user_id = request.POST.get('user_id')
#         user_pw = request.POST.get('user_pw')
        

#         #유효성 처리
#         res_data = {}
#         if not (user_id and user_pw):
#             res_data['error']="모든 칸을 다 입력해주세요."
#         else:
#             # 기존 DB에 있는 member 모델과 같은 값인 걸 가져옴.
#             member = Member.objects.get(user_id = user_id, user_pw=user_pw)

#             # 비밀번호가 맞는지 확인한다. 위에 check_password를 참조
#             if check_password(password, member.user_pw):
#                 #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장된다.
#                 request.session['user_id'] = member.user_id
                
#                 #리다이렉트
#                 return redirect('/')
#             else:
#                 res_data['error'] = "비밀번호가 틀렸습니다."
#         return render(request, 'signin.html', res_data)
#                 #응답 데이터 res_data 전달