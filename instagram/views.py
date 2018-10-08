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
    uploadform= ImageForm
    profile = User.objects.get(username=username)
    # print(profile.id)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    images = Image.get_profile_images(profile.id)
    title = f'@{profile.username} Instagram photos and videos'

    return render(request, 'main_pages/profile.html', {'title':title, 'profile':profile, 'profile_details':profile_details, 'images':images,'uploadform':uploadform})
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
        form = ProfileForm()
    return render(request, 'main_pages/edit_profile.html', {'form':form})
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
        uploadform = ImageForm(request.POST, request.FILES)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('profile', username=request.user)
    else:
        uploadform = ImageForm()
    
    return render(request, 'main_pages/profile.html', {'uploadform':uploadform})

# @login_required(login_url='/accounts/login')
# def single_image(request, image_id):
#     image = Image.get_image_id(image_id)
#     comments = Comments.get_comments_by_images(image_id)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.image = image
#             comment.user = request.user
#             comment.save()
#             return redirect('single_image', image_id=image_id)
#     else:
#         form = CommentForm()
        
#     return render(request, 'image.html', {'image':image, 'form':form, 'comments':comments})