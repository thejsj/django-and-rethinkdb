from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django_and_rethinkdb.forms.register import RegistrationForm
from django_and_rethinkdb.forms.login import LoginForm
import rethinkdb as r
import json

def main(request):
    return render(request, 'index.html')

def login(request):
    username = password = ''
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse('User %s logged in' % form.cleaned_data['username'])
        return HttpResonse('Error logging user in')
    raise PermissionDenied

def signup(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('User %s Created' % form.cleaned_data['username'])
        return HttpResonse('Error in SignUp')
    raise PermissionDenied

def config(request):
    config = {
        'ports': {
            'http': '8000',
        },
        'url': '127.0.0.1',
        'email': request.user.username
    }
    return HttpResponse('window.config = %s;' % json.dumps(config))
