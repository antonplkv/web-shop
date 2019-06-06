from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
# Create your views here.


def register(request):
    """
    This view registrates users in default
    django User model
    :param request:
    :return: adding new user to model
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'auth_app/signup.html', {'form': form})


def login(request):
    """
    As well as register but login :)
    :param request:
    :return: loginned user
    """

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        print(form.is_bound)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_password)
            auth_login(request, user)
            return redirect('/')
    else:

        form = AuthenticationForm()

    return render(request, 'auth_app/signup.html', {'form': form})

def log_out(request):
    """
    log out
    :param request:
    :return:
    """
    logout(request)
    return redirect('/')