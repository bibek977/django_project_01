from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("home page")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("phone")

        contact = Contact(name=name, email=email, phone=mobile)
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')