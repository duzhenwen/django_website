from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerForm
# Create your views here.
from django.contrib.auth import authenticate,login
from .models import user_infor
def Register(request):
    if request.method=='POST':
        user_infor.objects.create(username=request.POST['username'],telephone=request.POST['telephone'],email=request.POST['email'],password=request.POST['password'])
        return render(request,"begin/content.html")
    else:
       return render(request,"begin/register.html")

def Login(request):
    if request.method=='POST':
        form=registerForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)  
                return  render(request,'begin/content.html')
            else:
                return HttpResponse("SORRY")
    else:
        return  render(request,'begin/login.html')


    return render(request,'begin/login.html')

def content(request):
    return render(request,'begin/content.html')
