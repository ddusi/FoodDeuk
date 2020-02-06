from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import *

def like(request): #좋아요 리스트 화면
    return render(request, 'mainapp/like.html', {})

def mypage(request): #마이페이지
    return render(request,
    'mainapp/mypage.html',
    {})

def about(request): #어바웃 페이지
    return render(request, 'mainapp/about.html', {})

def detail(request, r_code): #음식점 상세페이지 O
    return render(request, 'mainapp/detail/%s.html' % r_code,{})
    #후에 return render(request, 'mainapp/detail.html',{mysite의 detail.html 참고})
#모델에 food_id 존재후 작성가능

def swipe(request):  # 스와이프 화면
    R = Restaurant.objects.all()[:20]
   # 1개 get, 원하는것만 filter
    print(R[0].r_img)
    return render(
    request,
    'mainapp/swipe.html',
    {'Restaurants': R})


def recognition(request):
    Mylatitude = request.GET.get('latitude')
    Mylongitude = request.GET.get('longitude')
    sql = 'SELECT *, (6371*acos(cos(radians('+Mylatitude+'))*cos(radians(longitude))*cos(radians(Latitude)-radians('+Mylongitude+'))+sin(radians('+Mylatitude+'))*sin(radians(longitude)))) AS distance FROM Restaurant HAVING distance <= 1 ORDER BY distance LIMIT 0,300'
    res = Restaurant.objects.raw(sql)

    res_json = serializers.serialize('json', res)   
    return HttpResponse(res_json, content_type='application/json')
