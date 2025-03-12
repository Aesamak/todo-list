from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from todo import models
from todo.models import todoo
from django.contrib.auth import authenticate,login,logout,decorators
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        frm=request. POST.get('fnm')
        emailid=request.POST.get('email')
        pwd=request.POST.get('pwd')
        my_user=User.objects.create_user(frm, emailid, pwd)
        my_user.save()
        return redirect('/login')

    return render(request,'signup.html')

def loginn(request):
    if request.method=='POST':
        fnm=request.POST.get('fnm')
        pwd=request.POST.get('pwd')
        print(fnm, pwd)
        userr=authenticate(request,username=fnm,password=pwd)
        if userr is not None:
            login(request,userr)
            return redirect('/todopage')
        else:
            return redirect('/loginn')
    return render(request,'loginn.html')

@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        print(title)
        obj=models.todoo(tital=title,user=request.user)
        obj.save()
        user=request.user        
        res=models.todoo.objects.filter(user=user).order_by('-date')
        return redirect('/todopage',{'res':res})
        
    
    res=models.todoo.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html',{'res':res,})

@login_required(login_url='/login')
def delete_todo(request,srno):
    print(srno)
    obj=models.todoo.objects.get(srno=srno)
    obj.delete()
    return redirect('/todopage')

@login_required(login_url='/login')
def edit_todo(request, srno):
    if request.method == 'POST':
        title = request.POST.get('title')
        print(title)
        obj = models.todoo.objects.get(srno=srno)
        obj.tital = title
        obj.save()
        return redirect('/todopage')

    obj = models.todoo.objects.get(srno=srno)
    return render(request, 'edit_todo.html', {'obj': obj})


def signout(request):
    logout(request)
    return redirect('/login')