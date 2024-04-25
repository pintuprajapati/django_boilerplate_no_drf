from django.shortcuts import render

# Create your views here.
def login(request):
    print("You are inside Login Function")
    return render(request, 'authentication/login.html')