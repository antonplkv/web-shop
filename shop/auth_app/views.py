from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
import redis
# Create your views here.
from .utils import tracker


def empty_cart(user_id):
    """

    :param user_id: unique user id
    :return: True result if everything ok
    """
    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    r.delete(str(user_id))


def swap_id(request, unique_id):
    """
    Swap session id products to user id
    :param request:
    :return:
    """

    r = redis.StrictRedis(host='localhost', port=6379, db=1)
    products = r.get(str(unique_id))

    if products:
        r.set(request.user.id, products)
    else:
        return None

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
            swap_id(request, tracker(request))
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
        if form.is_valid():
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=my_password)
            auth_login(request, user)
            swap_id(request, tracker(request))
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
    empty_cart(request.user.id)
    return redirect('/')



