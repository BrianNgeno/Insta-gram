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

def logout(request):
    return render(request, 'main_pages/home.html')

def view_image(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{"image":image})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})
