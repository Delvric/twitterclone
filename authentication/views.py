from django.shortcuts import render, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from authentication.forms import LoginForm, SignUpForm


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                 username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def signupview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage')))
    form = SignUpForm()
    return render(request, 'generic_form.html', {'form': form})


@login_required
def index(request):
    return render(request, 'index.html')


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
