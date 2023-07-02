from django.shortcuts import render, HttpResponse
from firstapp.models import Contact
from django.contrib import messages
#from datetime import datetime

# Create your views here. 

def index(request):
    context = {
        "variable" : "This is HUMINGO.....!!"
    }
  #  messages.success(request, "this is a test message")
    return render(request, "index.html", context) 
    # return HttpResponse("This is home page")

def about(request):
    return render(request, "about.html", )
    #return HttpResponse("THIS IS ABOUT PAGE") isse sirf response jayega render nhi hoga block page

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = int(request.POST.get('phone'))
        desc = request.POST.get('desc')
        contact = Contact(name= name, email= email, phone= phone, desc= desc)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, "contact.html")

def service(request):
    return render(request, "service.html")






# contact = Contact(name= name)-- isse contact ye sab register honge
# contact.save()-- isse contact kasara data save ho jayega 
# messages.sucess(...) -- this is for djnago messages alert 