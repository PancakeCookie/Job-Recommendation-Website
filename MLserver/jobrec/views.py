from django.shortcuts import render, redirect
from deep.test import jobRec
from users.models import User

# Create your views here.

def index(request):
    if request.method == 'GET':

        session_id = request.session['useremail']
        user_info = User.objects.get(useremail=session_id)
        res_data = {
            'nickname': user_info.nickname
        }

        return render(request, 'jobrec/test_1.html',res_data)

    elif request.method == 'POST':

        answer_li=[]
        data =request.POST

        answer_li.append(int(data.get('aq4_2'.rstrip())))
        answer_li.append(int(data.get('aq11_2'.rstrip())))
        answer_li.append(int(data.get('aq16_2'.rstrip())))
        answer_li.append(int(data.get('aq18_2'.rstrip())))
        answer_li.append(int(data.get('aq19_2'.rstrip())))
        answer_li.append(int(data.get('aq22_2'.rstrip())))
        answer_li.append(int(data.get('aq23_2'.rstrip())))
        answer_li.append(int(data.get('aq32_2'.rstrip())))
        answer_li.append(int(data.get('aq35_2'.rstrip())))
        answer_li.append(int(data.get('aq39_2'.rstrip())))
        answer_li.append(int(data.get('aq40_2'.rstrip())))
        answer_li.append(int(data.get('cq2'.rstrip())))
        answer_li.append(int(data.get('cq8'.rstrip())))
        answer_li.append(int(data.get('cq15'.rstrip())))
        answer_li.append(int(data.get('cq16'.rstrip())))
        answer_li.append(int(data.get('cq17'.rstrip())))
        answer_li.append(int(data.get('cq29'.rstrip())))
        answer_li.append(int(data.get('cq34'.rstrip())))
        answer_li.append(int(data.get('cq39'.rstrip())))
        answer_li.append(int(data.get('cq44'.rstrip())))
        answer_li.append(int(data.get('cq46'.rstrip())))
        answer_li.append(int(data.get('cq47'.rstrip())))
        answer_li.append(int(data.get('cq49'.rstrip())))
        answer_li.append(int(data.get('iq1'.rstrip())))
        answer_li.append(int(data.get('iq3'.rstrip())))
        answer_li.append(int(data.get('iq4'.rstrip())))
        answer_li.append(int(data.get('iq6'.rstrip())))
        answer_li.append(int(data.get('sq12'.rstrip())))
        answer_li.append(int(data.get('sq15'.rstrip())))
        answer_li.append(int(data.get('kq1_2'.rstrip())))
        answer_li.append(int(data.get('kq2_2'.rstrip())))
        answer_li.append(int(data.get('kq3_2'.rstrip())))
        answer_li.append(int(data.get('kq4_2'.rstrip())))
        answer_li.append(int(data.get('kq5_2'.rstrip())))
        answer_li.append(int(data.get('kq6_2'.rstrip())))
        answer_li.append(int(data.get('kq7_2'.rstrip())))
        answer_li.append(int(data.get('kq8_2'.rstrip())))
        answer_li.append(int(data.get('kq9_2'.rstrip())))
        answer_li.append(int(data.get('kq10_2'.rstrip())))
        answer_li.append(int(data.get('kq11_2'.rstrip())))
        answer_li.append(int(data.get('kq12_2'.rstrip())))
        answer_li.append(int(data.get('kq13_2'.rstrip())))
        answer_li.append(int(data.get('kq14_2'.rstrip())))
        answer_li.append(int(data.get('kq15_2'.rstrip())))
        answer_li.append(int(data.get('kq16_2'.rstrip())))
        answer_li.append(int(data.get('kq17_2'.rstrip())))
        answer_li.append(int(data.get('kq21_2'.rstrip())))
        answer_li.append(int(data.get('kq24_2'.rstrip())))
        answer_li.append(int(data.get('kq25_2'.rstrip())))
        answer_li.append(int(data.get('kq26_2'.rstrip())))
        answer_li.append(int(data.get('kq30_2'.rstrip())))
        answer_li.append(int(data.get('kq31_2'.rstrip())))
        answer_li.append(int(data.get('kq33_2'.rstrip())))
        answer_li.append(int(data.get('saq1_2'.rstrip())))
        answer_li.append(int(data.get('saq3_2'.rstrip())))
        answer_li.append(int(data.get('saq5_2'.rstrip())))
        answer_li.append(int(data.get('saq6_2'.rstrip())))
        answer_li.append(int(data.get('saq7_2'.rstrip())))
        answer_li.append(int(data.get('saq20_2'.rstrip())))
        answer_li.append(int(data.get('saq26_2'.rstrip())))
        answer_li.append(int(data.get('saq28_2'.rstrip())))
        answer_li.append(int(data.get('saq30_2'.rstrip())))
        answer_li.append(int(data.get('saq31_2'.rstrip())))
        answer_li.append(int(data.get('saq35_2'.rstrip())))
        answer_li.append(int(data.get('saq36_2'.rstrip())))
        answer_li.append(int(data.get('saq38_2'.rstrip())))
        answer_li.append(int(data.get('saq39_2'.rstrip())))
        answer_li.append(int(data.get('saq43_2'.rstrip())))
        answer_li.append(int(data.get('vq3'.rstrip())))
        answer_li.append(int(data.get('vq6'.rstrip())))


        # jobRec(answer_li)

        test_result = jobRec(answer_li)
        session_id = request.session['useremail']
        member = User.objects.get(useremail=session_id)
        member.rec_cate1=test_result[0]
        member.rec_cate2=test_result[1]
        member.rec_cate3=test_result[2]
        member.save()
        # 전송받은 이메일 비밀번호 확인
        return redirect('/jobrec/result')


def result(request):
    session_id = request.session['useremail']
    user_info = User.objects.get(useremail=session_id)

    context={'rec_cate1' : user_info.rec_cate1,
             'rec_cate2' :user_info.rec_cate2,
             'rec_cate3':user_info.rec_cate3}

    return render(request, 'jobrec/jobrec_result.html',context)