from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from mainapp.models import *
from scipy.spatial import distance
from django.utils import timezone




def like(request): #좋아요 리스트 화면
    return render(request, 'mainapp/like.html', {})

def mypage(request): #마이페이지
    return render(request,
    'mainapp/mypage.html',
    {})

def about(request): #어바웃 페이지
    return render(request, 'mainapp/about.html', {})

def detail(request, r_id): #음식점 상세페이지 O
    return render(request, 'mainapp/detail/%s.html' %r_id,{})
    #후에 return render(request, 'mainapp/detail.html',{mysite의 detail.html 참고})
#모델에 food_id 존재후 작성가능

def swipe(request):  # 스와이프 화면
    R = Restaurant.objects.all()[:20]
    return render(
    request,
    'mainapp/swipe.html',
    {'Restaurants': R})


def recognition(request):
    Mylatitude = request.GET.get('latitude')
    Mylongitude = request.GET.get('longitude')
    sql = '''SELECT *, (6371*acos(cos(radians(''' + Mylatitude + '''))*cos(radians(latitude))*cos(radians(longitude)
    -radians('''+Mylongitude+'''))+sin(radians('''+Mylatitude+'''))*sin(radians(latitude))))
     AS distance FROM Restaurant HAVING distance <= 20 ORDER BY distance LIMIT 0,300'''
    res = Restaurant.objects.raw(sql)# SQL 문에서 반경 20KM 이내 값만 조회하여 가져옴
    res_json = serializers.serialize('json', res)   
    return HttpResponse(res_json, content_type='application/json')

def likeornot(request):
    Tlike_dislike = LikeDislike()# DB테이블 내역 불러와 Tlike_dislike에 저장
    member_id = request.session['user_id']# 현재 로그인되어 있는 정보 가져옴
    res_id = request.GET.get('r_id')# main.js 에서 ajax로 보낸 식당id 값 저장
    like_dis = request.GET.get('like_dislike')#main.js에서 ajax로 보낸 like_dislike 값 저장

    member = Member.objects.get(user_id=member_id)# DB 테이블(Member)에서 user_id 가 member_id와 동일한 내용 조회하여 저장
    Tlike_dislike.m = member #like_dislike DB에 조회한 member값 입력
   
    rest = Restaurant.objects.get(pk=res_id) # 입력받은 식당 관련 내역 DB 조회하여 입력
    Tlike_dislike.r = rest # like_dislike DB에 저장

    Tlike_dislike.like_dislike = like_dis# 테이블의 like_dislike 속성 값에 like_dis값 입력
    Tlike_dislike.day = timezone.now()# 테이블의 day 속성 값에 현재시간 입력

    Tlike_dislike.save()
    return HttpResponse('DB입력 OK')

def load_likeornot(request):
    sql = '''select restaurant.id,restaurant.r_name,restaurant.r_img,restaurant.r_kind,restaurant.des,restaurant.address,restaurant.address_road,restaurant.latitude,restaurant.longitude,restaurant.closetime,restaurant.number from restaurant join like_dislike on restaurant.id = like_dislike.r_id where like_dislike=1;'''
    likeres = Restaurant.objects.raw(sql)# SQL 문에서 반경 20KM 이내 값만 조회하여 가져옴
    likeres_json = serializers.serialize('json', likeres) 
    return HttpResponse(likeres_json, content_type='application/json')
