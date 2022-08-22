from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username', None)
            messages.success(
                request, f'Welome {username}, your account has been created!')
            return redirect('login')

    form = RegisterForm()
    return render(request, 'users/register.html', context={
        'form': form
    })


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
