from django.shortcuts import render,redirect
from .models import User_message

# Create your views here.

def index(request):

    if request.method == "POST":

        name=request.POST['name']
        last_name=request.POST['last_name']
        text = request.POST['text']

        email = request.POST['email']

        mes = User_message.objects.create(name=name,last_name=last_name,email=email,text=text)
        mes.save()

        return redirect('/')

        
    else:
        return render(request,'index.html')




    