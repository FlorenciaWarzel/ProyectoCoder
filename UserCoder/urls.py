from django.urls import path

from UserCoder.views import *

urlpatterns = [
    path('login', login_request, name='UserLogin'),
    path('registro', registro, name='UserRegistro'),
]