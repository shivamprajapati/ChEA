from django.http import HttpResponse
from django.template  import loader
from django.shortcuts import get_object_or_404, render
from .models import People, Bio



def index(request):
      all_members = People.objects.all()
      context={ 'all_members' :all_members }
      return render(request, 'members/index.html', context)



def detail(request, id):
        member= get_object_or_404(People, kwargs = id)
        return render(request, 'members/detail.html' , {'member' : member})