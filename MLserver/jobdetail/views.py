from django.shortcuts import render

# Create your views here.
from users.models import MiddleCate

def main(request):


    return render(request, 'jobdetail/icons.html')