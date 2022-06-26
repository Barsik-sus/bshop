from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout


def loginView(request):
    login_status = ""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        print('do logining')
        print(user_form.errors)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.GET:
                        return redirect(request.GET['next'])
                    return redirect('home')
            login_status = 'Incorrect login or password'
    else:
        user_form = UserLoginForm()
    context = {
        "title":"Login",
        "logedin": request.user.is_authenticated,
        "dologin": True,
        "user_form": user_form,
        "status": login_status,
    }
    print(request.user.is_authenticated)
    return render(request, 'login/index.html', context)

def sign_upView(request):
    sign_up_status = ''
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            if 'next' in request.GET:
                    return redirect(request.GET['next'])
            return redirect('home')
        sign_up_status = "".join(user_form.errors.popitem()[1])
    else:
        user_form = UserRegistrationForm()
    context = {
        "title":"Sign-up",
        "logedin": request.user.is_authenticated,
        "dologin": False,
        "user_form": user_form,
        "status": sign_up_status,
    }
    return render(request, 'login/index.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')