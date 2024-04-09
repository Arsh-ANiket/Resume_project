from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "myapp/home.html")

def candidate_register(request):
    return render(request,"myapp/candidateregister.html")

def organization(request):
    return render(request,"myapp/org.html")

def organization_signup(request):
    return render(request,"myapp/orgsignup.html")

def organization_signin(request):
    return render(request,"myapp/orgsignin.html")