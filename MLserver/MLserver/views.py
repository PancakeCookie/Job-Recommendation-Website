from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

from users.models import User
from discover.models import knowcode

def index(request) :
    know_all = knowcode.objects.all()
    know20 = knowcode.objects.filter(year=2020).order_by('large_level')
    context = {
        'know20': know20,
        'know_all': know_all
    }
    try :
        session_id = request.session["useremail"]
        if session_id :
            user_info = User.objects.get(useremail=session_id)
            context['session'] = session_id
            context['userinfo'] = user_info
    except :
        pass
    return render(request, 'index.html', context)

def ajax_method(request):
    receive_message = request.GET.get('year_str')
    # print('리시브 : ',receive_message)
    # know20 = list(knowcode.objects.filter(year=2020).order_by('large_level').values())
    # know19 = list(knowcode.objects.filter(year=2019).order_by('large_level').values())
    # know18 = list(knowcode.objects.filter(year=2018).order_by('large_level').values())
    # know17 = list(knowcode.objects.filter(year=2017).order_by('large_level').values())
    know = list(knowcode.objects.filter(year=receive_message).order_by('large_level').values())
    # print('views : ',know)
    send_message = {
        'know' : know
    }
    return JsonResponse(send_message)


