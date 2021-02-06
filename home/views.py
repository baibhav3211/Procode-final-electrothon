from django.shortcuts import render
from django.contrib import messages 
from articles.models import Post
from home.models import Contact, Subscribe

# Create your views here.
def home(request):
    if request.method=="POST":
        email=request.POST['email']
        if len(email)<3:
            messages.error(request, "Please fill the email correctly")
        else:
            subscribe=Subscribe(email=email)
            subscribe.save()
            
            messages.success(request, "Your subscription has been successfully accepted!")
    return render(request, 'home/home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

def dashboard(request):
    allArticles= Post.objects.all().filter(category=3)
    allCoding= Post.objects.all().filter(category=2)
    allRobotics= Post.objects.all().filter(category=1)
    context={'allArticles': allArticles,'allCoding': allCoding,'allRobotics': allRobotics}
    return render(request, 'home/dashboard.html', context)
def setting(request):
    return render(request, 'home/prof_settings.html')