from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response
from .tokens import account_activation_token
from .models import *
from .serializer import AccountRegisterSerializer
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework import views

class AccountRegisterView(views.APIView):
    def get(self,*args,**kwargs):
        return Response({'data':{'name':'examplename',
                                 'username':'exampleusername',
                                 'last_name':'examplelast_name',
                                 'email':'example@email.ru',
                                 'password':'password',
                                 'password2':'password2'
                                 }})

    def post(self,request,*args,**kwargs):
        serializer = AccountRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer.save()
            current_site=get_current_site(request)
            subject = 'OGOGO dev. team'
            message = render_to_string('register/activation.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = serializer.data['email']
            email = EmailMessage(subject,message,to=[to_email,])
            email.send()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountLoginView(views.APIView):
    def post(self,request,*args,**kwargs):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return Response({'data':'succes'})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
