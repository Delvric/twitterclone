from django.shortcuts import render, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from authentication.forms import LoginForm, SignUpForm

from django.views.generic import TemplateView


class Loginview(TemplateView):
    def get(self, request, **kwargs):
        form = LoginForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', ))


class Signupview(TemplateView):
    def get(self, request, **kwargs):
        form = SignUpForm()
        return render(request, 'generic_form.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))


@login_required
def index(request):
    return render(request, 'index.html')


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
