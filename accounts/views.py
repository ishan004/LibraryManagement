from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
import re
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


# Create your views here.

class RegistrationForm(forms.Form):
    
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    

def admin_register(request):
    
    if request.user.is_authenticated:
        return redirect('admindashboard')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Additional email validation using a regular expression
            
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]{2,29}$', username):
                form.add_error('first_name', 'Invalid format')
                
            if not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
                form.add_error('email', 'Invalid email format')

                return render(request, 'accounts/register.html', {'form': form})

            user_obj = User.objects.filter(username=email)
            if user_obj.exists():
                messages.warning(request, "Email already registered")
                return HttpResponseRedirect(request.path_info)

            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()

            messages.success(request, "An user has been registered.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admindashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username= username)
        
        if not user_obj.exists():
            messages.warning(request, "Account does not exist")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=username, password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('admindashboard')
        
        messages.warning(request, "Invalid username or password")
        return HttpResponseRedirect(request.path_info)
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')
