from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Condition, News, Usluga,Team,Boss,TeamAbout, List, Gallery
from apps.contacts.models import Contacts,PageContact

# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.all()
    condiction = Condition.objects.latest('id')
    news = News.objects.all()
    usluga = Usluga.objects.all()
    team = Team.objects.all()
    boss = Boss.objects.latest('id')

    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    return render(request, 'base/index.html', locals())

def about(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.all()
    condiction = Condition.objects.latest('id')
    news = News.objects.all()
    usluga = Usluga.objects.all()
    team = Team.objects.all()
    boss = Boss.objects.latest('id')


    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)

    return render(request, 'about.html', locals())


def team(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.all()
    team_about = TeamAbout.objects.all()

    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)

    return render(request, 'team.html', locals())

def gallery(request):
    settings = models.Settings.objects.latest('id')
    slide = models.Slide.objects.all()
    gallery = Gallery.objects.all()
    
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    return render(request, 'gallery.html', locals())


def list_price(request):
    settings = models.Settings.objects.latest('id')
    list = List.objects.latest('id')
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)               

    return render(request, 'list.html', locals())

def news(request):
    news = News.objects.all()
    settings = models.Settings.objects.latest('id')


    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data) 
    return render(request, 'news.html', locals())

def contact(request):
    settings = models.Settings.objects.latest('id')
    
    if request.method=="POST":
        if 'bron_form' in request.POST:
            name = request.POST.get('name')
            number = request.POST.get('number')
            data = request.POST.get('data')
            contacts = Contacts.objects.create(name=name, number=number, data=data) 
        if 'contact_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            page_contact = PageContact.objects.create(name=name, email=email, number=number,  subject=subject, message=message)
    return render(request, 'contact.html', locals())


def blog_news(request, id):
    settings = models.Settings.objects.latest('id')
    blog = News.objects.get(id=id)
    

    return render(request, 'post.html', locals())

