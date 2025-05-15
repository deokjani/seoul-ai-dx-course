from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="member_index"),
    ###################################################################################################
    # 회원 관리 URL
    ###################################################################################################
    # 회원 리스트
    path("", views.member_list, name="member_list"),
    # 회원데이터 추가 / 저장
    path("add/", views.member_add, name="member_add"),
    path("add/save/", views.member_add_save, name="member_add_save"),
    # 회원데이터 삭제
    path("delete/<int:id>/", views.member_delete, name="member_delete"),
    
    ###################################################################################################
    # 카메라 제어
    ##################################################################################################
]