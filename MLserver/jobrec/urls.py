from django.urls import path, include

import jobrec.views


urlpatterns = [
    path('submit', jobrec.views.index),
    path('result', jobrec.views.result),
]