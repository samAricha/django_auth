from msilib.schema import Feature
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    features= Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username Already used')
                return redirect('register')
            else:
                User = User.objects.create_user(username=username, email=email, password=password)
                User.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect ('register')
    else:   
        return render(request, 'register.html')
        
    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
