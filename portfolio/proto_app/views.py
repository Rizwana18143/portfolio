from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def contact(request):
    return render(request,'contact.html')
def project(request):
    return render(request,'project.html')
def skills(request):
    return render(request,'skills.html')
def internships(request):
    return render(request,'internships.html')
def footer(request):
    return render(request,'footer.html')
# def Education(request):
#     return render(request,'Education.html')
def index(request):
    return render(request,'index.html')
def navbar(request):
    return render(request,'navbar.html')