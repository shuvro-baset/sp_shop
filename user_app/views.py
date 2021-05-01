from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('user_app:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("user: ",user)
            # user_id = user.id
            # print("user_id: ", user_id)
            if user is not None:
                login(request, user)
                return redirect('user_app:home')
            else:
                # messages.info(request, 'Username or Password incorrect')
                return render(request, "login.html", )
        context = {}
        return render(request, "login.html", context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('user_app:home')
    else:
        if request.method == 'POST':
            print("yes I am heating")
            username = request.POST.get("username")
            password = request.POST.get("password")
            email = request.POST.get("email")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            print("user: ", user)
            return redirect('user_app:login')

        context = {}
    return render(request, "signup.html", context)


def logoutUser(request):
    user = request.user
    print("user: ", user.id)
    logout(request)

    return redirect('user_app:home')