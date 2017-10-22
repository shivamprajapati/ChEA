from django.shortcuts import render
from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import get_object_or_404, render
from . models import Mags, Cont

def index(request):
      all_magzines = Mags.objects.all()
      context={ 'all_magzines' :all_magzines }
      return render(request, 'magzine/index.html', context)
