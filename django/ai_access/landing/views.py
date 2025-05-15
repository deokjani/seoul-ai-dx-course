from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("안녕하세요. landing 앱입니다.")
    sendData = {
        "titles": "인공지능 출입관리 프로젝트",
        "sub_titles": "Face Recognition, Dlib, CNN, FAISS, OpenCV",
        "state_msg": "서비스 시작하기",
    }    
    
    return render(request, "landing/main.html", sendData)