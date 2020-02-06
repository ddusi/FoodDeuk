from django.urls import path, include
from . import views
from mainapp.main import views as main_views
from mainapp.swipe import views as swipe_views

# /main 으로 시작하는 하위 url 설정
main_patterns = [
    path('',main_views.main),
    path('signup/', main_views.signup, name='signup'),
    path('signin/', main_views.signin, name='signin'),
]

# /swipe 으로 시작하는 하위 url 설정
swipe_patterns = [
    path('', swipe_views.swipe),
    path('mypage/', swipe_views.mypage, name='mypage'),
    path('detail/<int:id>', swipe_views.detail, name='detail'),
    path('like/', swipe_views.like, name='like'),
    path('about/', swipe_views.about, name='about'),
]

# 변수로 설정한 값을 include함.
urlpatterns = [
    path('main/', include(main_patterns)),
    path('swipe/', include(swipe_patterns)),
    ]
