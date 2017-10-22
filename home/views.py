from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate , login , logout
from . form import UserForm
from django.views import generic
from django.views.generic import View
from .models import Events , Eve_pics





def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else :
       upcoming = Events.objects.all()
       return render(request, 'home/index.html', {'upcoming' : upcoming })

def events(request):
 event = Events.objects.get(pk=1);
 return render(request, 'home/events.html', {'event' : event})

def about(request):
 return render(request, 'home/about.html', {})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                upcoming = Events.objects.all()
                userinfo= request.user
                return render(request, 'home/index.html', {'upcoming' : upcoming,'userinfo': userinfo})
            else:
                return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login.html')

class UserFormView(View):
    form_class= UserForm
    template_name= 'home/registration_form.html'
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
             user = form.save(commit=False)
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user.set_password(password)
             user.save()
             user = authenticate(username=username, password=password)
             if user is not None:
               if user.is_active:
                 login(request, user)

                 return render(request, 'home/index.html', )
        context = {
        "form": form,
              }
        return render(request, 'home/registration_form.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'home/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'home/registration_form.html', context)

def forum(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
      return render(request, 'home/forum.html', {})



