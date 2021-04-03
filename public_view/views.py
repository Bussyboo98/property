from django.shortcuts import render
from django.http import HttpResponse 
from public_view.models import *
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return  render(request,'frontend/index.html')

def about(request):
    about = Team.objects.all() 
    return  render(request,'frontend/about.html',{'abt': about})

def about_detail(request, abt_id):
    detail = Team.objects.get(id=abt_id)
    return render(request, 'frontend/about-detail.html', {'det':detail})

def rent(request):
    return  render(request,'frontend/view-list.html')

def agent(request):
    return  render(request,'frontend/agent.html')

def request(request):
    return  render(request,'frontend/request.html')

def register(request):
    return  render(request,'frontend/register.html')

def sale(request):
    return  render(request,'frontend/view-list.html')

def offer(request):
    return  render(request,'frontend/view-list.html')


    