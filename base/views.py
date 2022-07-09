from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import NewsArtical, NewspaperTitle, NewsComment
from .forms import NewsPaperForm, UserForm

def userLogin(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Incorrect credentials!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect credentials!')

    data = {'page':'loginPage'}
    return render(request, 'base/login.html', data)

@login_required(login_url="login")
def userLogout(request):
    logout(request)
    return redirect('home')

def userRegister(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid data')

    data = {'page':'register', 'form': form}
    return render(request, 'base/login.html', data)

@login_required(login_url="login")
def home(request):
    newspaperName = request.GET.get('newspapername') if request.GET.get('newspapername') != None else ''
    newspapers = NewsArtical.objects.filter(newspaperTitle__name__icontains=newspaperName)
    newspaperTitles = NewspaperTitle.objects.all()
    data = {'newspapers':newspapers, 'newspaperTitles': newspaperTitles}
    return render(request, 'base/home.html', data)

@login_required(login_url="login")
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    newspapers = user.newsartical_set.all()
    data = {'user': user, 'newspapers':newspapers}
    return render(request, 'base/userProfile.html', data)

@login_required(login_url="login")
def newspaper(request, pk):
    newspaper1 = None
    newspaper1 = NewsArtical.objects.get(id=pk)
    userComments = newspaper1.newscomment_set.all().order_by('-updatedAt')

    if request.method == 'POST':
        userComment = NewsComment.objects.create(
            user=request.user,
            newspaper=newspaper1,
            commentInfo=request.POST.get('commentInfo')
        )
        return redirect('newspaper', pk=newspaper1.id)

    selectedNewsPaper = {'newspaper': newspaper1, 'userComments':userComments}
    return render(request, 'base/newspaper.html', selectedNewsPaper)

@login_required(login_url="login")
@permission_required('is_staff', )
def newspaper_create(request):
    form = NewsPaperForm()
    if request.method == 'POST':
        form = NewsPaperForm(request.POST)
        if form.is_valid:
            newspaper = form.save(commit=False)
            newspaper.newsAdmin = request.user
            newspaper.save()
            return redirect('home')

    createdNewsPaper = {'form': form}
    return render(request, 'base/form_newspaper.html', createdNewsPaper)

@login_required(login_url="login")
def newspaper_update(request, pk):
    newspaper = NewsArtical.objects.get(id=pk)
    form = NewsPaperForm(instance=newspaper)
    if request.method == 'POST':
        form = NewsPaperForm(request.POST, instance=newspaper)
        if form.is_valid:
            form.save()
            return redirect('home')

    updateNewsPaper = {'form': form}
    return render(request, 'base/form_newspaper.html', updateNewsPaper)

@login_required(login_url="login")
def newspaper_delete(request, pk):
    newspaper = NewsArtical.objects.get(id=pk)
    if request.method == 'POST':
        newspaper.delete()
        return redirect('home')

    return render(request, 'base/common_delete.html', {'delete_data': newspaper})

@login_required(login_url="login")
def update_user(request):
    form = UserForm(instance=request.user)
    data = {"form": form}
    return render(request, 'base/edit-user.html', data)