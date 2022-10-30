from django.shortcuts import render, redirect
from django.views.generic import CreateView

# from Onlineportal.student.models import std_data
from .forms import RegisterForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import teacher_data
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def teacher_acc(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = teacher_data() 
            obj.username = form.cleaned_data['username']
            obj.firstname = form.cleaned_data['firstname']
            obj.lastname = form.cleaned_data['lastname']
            obj.email = form.cleaned_data['email']
            obj.password = form.cleaned_data['password1']
            obj.save()
            print(obj)
            return redirect('login2')
    context = {'form':form}
    return render(request, 'registration/register_teacher.html', context)

# def registerpage(request):
#     # if request.user.is_authenticated:
#     #     return redirect('home')
#     # else:
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login1')
#     context = {'form':form}
#     return render(request, 'registration/register.html', context)

def teacherloginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        user = teacher_data.objects.get(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            context = {'user':user}
            return render(request, 'index.html', context)
    context = {}
    return render(request, 'registration/login_teacher.html', context)


def logoutUser(request):
	logout(request)
	# return redirect('home')

