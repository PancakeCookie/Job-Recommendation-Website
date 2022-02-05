from django.shortcuts import render
from deep.test import jobRec


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'jobrec/test.html')

    elif request.method == 'POST':

        answer_li=[]
        data =request.POST
        print(data)
        answer_li.append(int(data.get('a1')))
        answer_li.append(int(data.get('a2')))
        answer_li.append(int(data.get('a3')))
        answer_li.append(int(data.get('a4')))
        answer_li.append(int(data.get('a5')))

        # jobRec(answer_li)

        print(jobRec(answer_li))


        # 전송받은 이메일 비밀번호 확인
        return render(request, 'jobrec/test.html')