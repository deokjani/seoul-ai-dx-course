from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse

from api.models import Members

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. member 앱입니다.")

def member_delete(request, id):
    # 회원 삭제
    # (SQL) DELETE FROM api_members WHERE id = id;
    # filter(id=id).delete()는 조건에 맞는 모든 객체를 삭제합니다.
    # 조건에 맞는 객체가 없어도 에러가 발생하지 않습니다.
    # get(id=id).delete()는 조건에 맞는 객체가 1개일 때만 삭제합니다.
    # 조건에 맞는 객체가 없으면 DoesNotExist 예외, 2개 이상이면 MultipleObjectsReturned 예외가 발생합니다.
    Members.objects.filter(id=id).delete()
    # 만약 아래처럼 사용하면:
    # member = Members.objects.get(id=id)
    # member.delete()
    # 위와 같이 get을 쓰면 반드시 1개만 삭제, 없거나 여러 개면 에러 발생

    return redirect("member_list")

def member_list(request):
    # 회원 목록 조회(역순)
    # (SQL) SELECT * FROM api_members ORDER BY id DESC;
    memList = Members.objects.all().order_by("-id")
    print("SQL : ", memList.query)
    # 데이터 확인
    for mem in memList:
        print("id :", mem.id)
        print("ids :", mem.ids) 
        print("username :", mem.username)
        print("password :", mem.password)
        print("email :", mem.email)
        print("phone :", mem.phone)
        print("cnts :", mem.cnts)
        print("first_dates :", mem.first_dates)
        print("first_ips :", mem.first_ips)

    return render(request, "member/member_list.html", {"data": memList})

def member_add(request):
    return render(request, "member/member_add.html")
    
def member_add_save(request):
    if request.method == "GET":
        return HttpResponse("정상적인 접근이 아닙니다.")

    # 입력된 데이터 저장
    ids = request.POST.get("ids", "")
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    
    print("ids :", ids)
    print("username :", username)
    print("password :", password)
    print("email :", email)
    print("phone :", phone)

    # 회원등록
    saveMember = Members()
    saveMember.ids = ids
    saveMember.username = username
    saveMember.password = password
    saveMember.email = email
    saveMember.phone = phone
    saveMember.cnts = 0
    saveMember.first_dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    saveMember.first_ips = get_client_ip(request)
    saveMember.save()

    return redirect("member_list")

