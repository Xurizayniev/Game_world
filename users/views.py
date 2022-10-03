from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm
# Create your views here.

class ContactView(TemplateView):
    template_name = 'contact.html'

class LoginView(TemplateView):
    template_name = 'register.html'

def loginview(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            raise ValidationError('Wrong username or password !')


    return render(request, 'login.html', context={
        'form': form
    })

def logout_view(request):
    logout(request)
    return redirect('user:login')



            


def logout_view(request):
    logout(request)
    return redirect('user:login')











def user_registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('user:login')
    
    return render(request, 'registration.html', context={
        'form': form
    })