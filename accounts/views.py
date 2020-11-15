from django.shortcuts import render, redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages

# Create your views here.

def form(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_pass = request.POST['Password']
        email = request.POST['email']

        if password == confirm_pass:
            if User.objects.filter(username = username).exists():
                messages.info(request ,"Username not available ")
                

            elif User.objects.filter(email = email).exists():
                messages.info(request ,"email is already there ")
                

            else:
                user = User.objects.create_user(email = email,password = confirm_pass,username = username)
                user.save();
                print("user saved")
                return redirect('/')

        else:    
            messages.info(request,"password not matching")

        return redirect('form')

    else:    
        return render(request, 'form.html')

    
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,"wrong details")
            return render(request, "login.html")
    
    
    else:
        return render(request, "login.html")

    
def logout(request):
    auth.logout(request)
    return redirect('/')