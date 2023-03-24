from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import *
from .forms import*

def post_list(request):
    posts=Post.objects.all()
    return render(request,'sbcoins/index.html',{'posts':posts})

def login_func(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('post_list')
    else:
        form=AuthenticationForm()
    return render(request,'sbcoins/login.html',{'form':form})

def user_log_out(request):
    logout(request)
    return redirect('post_list')

def user_register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('post_list')
    else:
        form=UserCreationForm()
    return render(request,'sbcoins/register.html',{'form':form})


def get_post(request,pk):
    post=Post.objects.get(id=pk)
    return render(request, 'sbcoins/post.html',{'post':post})

def new_post(request):
    if request.method=='POST':
        postform=PostForm(request.POST)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('post_list')
    else:
        postform=PostForm()
    return render(request, 'sbcoins/newpost.html',{'postform':postform})






# Create your views here.
