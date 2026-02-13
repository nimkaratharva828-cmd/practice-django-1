from django.shortcuts import render,HttpResponse

# Create your views here.
def login_view(request):
    print("Login view called")
    return HttpResponse("This is the login page")