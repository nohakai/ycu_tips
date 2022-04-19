from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from . forms import UserCreateForm
from django.views import View
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView
from . forms import UserCreateForm, LoginForm
# Create your views here


class IndexView(generic.TemplateView):
    template_name = 'top.html'


class RuleView(generic.TemplateView):
    template_name = 'rule.html'



#アカウント作成ビュー
class Create_account(CreateView):
    def post(self, request,*args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home/thread/list/')
        return render(request, 'create.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form,})

create_account  = Create_account.as_view()
    
#ログインビュー
class Account_login(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/home/thread/list/')
        return render(request, 'login.html', {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})
    
account_login = Account_login.as_view()
        