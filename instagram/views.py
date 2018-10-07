from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from .forms import ProfileForm, ImageForm
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/accounts/login/')
def home_page(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{'image':image})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    print(" the number is this")
    print(profile.id)
    userprofile = User.objects.get(username=username)
    form = ImageForm()
    try:
        profile_info = Profile.get_by_id(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
        image = Image.get_images(profile.id)
    return render(request, 'main_pages/profile.html',{'form':form, 'userprofile':userprofile, 'profile_info':profile_info, 'image':image})

    '''
    editing user profile fillform & submission
    '''
@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        fom = ProfileForm()
    return render(request, 'main_pages/edit_profile.html', {'uploadform':fom})
    '''
    logs out current user from account
    '''
def logout(request):
    return render(request, 'main_pages/home.html')

    '''
    returns all images uploaded
    '''
def view_image(request):
    image = Image.objects.all()
    return render(request, 'main_pages/home.html',{"image":image})

    '''
    searching for profile
    '''
def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profile = Profile.search_user(search_term)
        message = f'{search_term}'

        return render(request, 'main_pages/search.html',{'message':message, 'profile':profile})
    else:
        message = 'Enter term to search'
        return render(request, 'main_pages/search.html', {'message':message})

@login_required(login_url='/accounts/login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            upload.save()
            return redirect('current_profile')
    else:
        form = ImageForm()
    
    return render(request, 'main_pages/profile.html', {'form':form})
