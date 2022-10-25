from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from .models import Candidate
from .forms import CandidateForm

# from core.forms import UniversityForm
from .forms import AssignmentForm

# Create your views here.

def index(request): 
    # context = {'form': UniversityForm()}
    return render(request, 'index.html')

def register(request):
    msg = None
    if request.method == 'POST': 
        form =SignUpForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            msg = 'user created'
            return redirect('login') 
        else: 
            msg = 'form is not valid'
    else: 
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})

def login_view(request): 
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST': 
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin: 
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')   
            else: 

                msg='invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request, 'admin.html')

def customer(request):
    return render(request, 'customer.html')

def employee(request):
    return render(request, 'employee.html')

def create_assignment(request):
    form = AssignmentForm()
    return render(request, 'customer.html', {'form': form})

# READ
def data_read(request):
    context = {'data_read':Candidate.objects.all()}
    return render(request, "data_read.html", context)
# CREATE / UPDATE
def data_form(request, id = None):
    if request.method == "POST":
        if id == None:
            form = CandidateForm(request.POST)
        else:
            candidate = Candidate.objects.get(pk = id)
            form = CandidateForm(request.POST, instance = candidate)
        if form.is_valid():
            form.save()
        return redirect('/data')
    else:
        if id == None:
            form = CandidateForm()
        else:
            candidate = Candidate.object.get(pk = id)
            form = CandidateForm(instance = candidate)
        return render(request, "data_form.html", {'form':form})

# DELETE
def data_delete(request, candidate_id):
    candidate = Candidate.objects.get(id = candidate_id)
    candidate.delete()
    return redirect('/data')