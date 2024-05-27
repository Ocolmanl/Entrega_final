from django.shortcuts import render
from django.contrib. auth.views import LoginView
from .forms import CustomAuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    
def about(request):
    return render(request, 'core/about.html')