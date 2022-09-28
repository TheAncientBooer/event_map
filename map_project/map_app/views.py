from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import AuthForm, EventForm
from .models import Event


@login_required
def index(request):
    # if request.user.is_anonymous:
    #     return redirect('login')
    events = Event.objects.all()
    

    context = {
        "events": events,
        "form": EventForm()
    }

    return render(request, 'map_app/index.html', context)


@login_required 
def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event_item = Event()
            event_item.title = form.cleaned_data['title']
            #event_item.user = request.user
            event_item.save()

    return redirect('index')


def delete(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        if request.user == event.user:
            event.delete()
    except Event.DoesNotExist:
        pass
    
    return redirect('index')

def signup(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            auth.login(request, user)
            return render(request, 'map_app/signup.html')
        else:
            context = {
                'form': form
            }
            return render(request, 'map_app/signup.html', context)

    context = {
        'form': AuthForm()
    }
    return render(request, 'map_app/signup.html', context)


def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user != None:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect('index')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
        return render(request, 'map_app/login.html', context)

    context = {
        "form": AuthForm()
    }
    return render(request, 'map_app/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('index')
