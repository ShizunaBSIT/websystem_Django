from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm  # Ensure this form exists and is imported correctly
from django.contrib.auth.decorators import login_required

@login_required
def products(request):
    return render(request, 
                  'auth/products.html',
                  {'section': 'products'})  # Ensure 'products.html' exists in your templates directory
def user_login(request):
    form = LoginForm()  # Initialize the form to avoid UnboundLocalError

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')

    return render(request, 'auth/login.html', {'form': form})  # Always defined
