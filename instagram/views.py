from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile


# Create your views here.
@login_required(login_url='/accounts/login/')
def home_page(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{"image":image})

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'main_pages/profile.html')

@login_required(login_url='/accounts/login/')
def edit(request):
    return render(request, 'main_pages/edit_profile.html')

def logout(request):
    return render(request, 'main_pages/home.html')

def view_image(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{"image":image})


