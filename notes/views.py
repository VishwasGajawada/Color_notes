from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm,NoteForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginUser,logout as logoutUser

# Create your views here.

@login_required(login_url='about')
def index(request):
    user = request.user
    notes = Note.objects.filter(user = user)

    context ={"notes":notes}
    return render(request,'notes/index.html',context)

@login_required(login_url='login')
def add_note(request):
    user = request.user
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = user
            note.save()
            return redirect('/')
    context ={"form":form}
    return render(request,'notes/add_note.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                loginUser(request, user)
                return redirect('/')
            else:
                messages.add_message(request,'Username or Password is incorrect')
    # else:
    #     form = AuthenticationForm()
    context = {"form":form}
    return render(request,'notes/login.html',context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = UserCreationForm()
    if request.method == 'POST':    
        # print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
    context ={"form": form}
    return render(request,'notes/signup.html',context)

@login_required(login_url='login')
def logout(request):
    logoutUser(request)
    return redirect('login')

@login_required(login_url='login')
def edit_note(request,pk):
    note = Note.objects.get(id=pk)
    if note.user!=request.user:
        return redirect('access_error')    
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={"form": form,"note":note}
    return render(request,'notes/edit_note.html',context)

@login_required(login_url='login')
def delete_note(request,pk):
    note = Note.objects.get(id=pk)
    if note.user!=request.user:
        return redirect('access_error')
    if request.method == 'POST':
        note.delete()
        return redirect('/')
    context ={"note":note}
    return render(request,'notes/delete_note.html',context)

def about(request):
    return render(request,'notes/about.html')

def access_error(request):
    return render(request,'notes/no_access.html')