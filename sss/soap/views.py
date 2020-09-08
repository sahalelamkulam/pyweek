from django.shortcuts import render
from .models import certificate

def index(request):
    return render(request,'soap/hello.html')

def git_fetch(request):
        try:
            email=request.POST["email"]
            a=certificate.objects.get(email=email)
            name = a.name.replace(" ", "%20")
            url="https://github.com/niranjanneeru/Pyweek-Temp/blob/master/assets/img/"+name+".png?raw=true"
            return render(request,'soap/base.html',{"url":url})
        except:
            return render(request,'soap/no_user.html')
