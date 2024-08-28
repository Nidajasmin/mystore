from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class GoodmorningView(APIView):

    def get(self,request,*args,**kw):
        return Response (data="Hello GoodMorning")
    

class GoodeveningView(APIView):
    def get(self,request,*args,**kw):
        return Response (data="Hello Goodevening")
    
class currentdateView(APIView):
    def get(self,request,*args,**kw):
        return Response (data="2024-01-19")

class todayView(APIView):

    def get(self,request,*args,**kw):
        time_now=datetime.now()
        return Response (data=time_now)
    
class justView(APIView):

    def get(self,request,*args,**kw):
        time_now=datetime.today()
        return Response (data=time_now)
    
class addView(APIView):
    def post(self,request,*args,**kw):
        print(request.data) 
        a=(request.data.get('num1')) 
        b=(request.data.get('num2'))
        c=int(a)+int(b)
        return Response(data=c)
    
class substractView(APIView):
    def post(self,request,*args,**kw):
        print(request.data) 
        a=int(request.data.get('num1'))
        b=int(request.data.get('num2'))

        if int(a)>int(b) :
          c=a-b
        else:
           c=b-a
        return Response(data=c)
    
class cubeView(APIView):
    def post(self,request,*args,**kw):
        print(request.data) 
        a=int(request.data.get('num1'))
        c=a**3
        return Response(data=c)
         
    


        