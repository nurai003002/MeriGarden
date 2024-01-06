from typing import Any
from django.shortcuts import render,redirect
from apps.base import models
from apps.secondary.models import Condition, News, Usluga,Team,Boss,TeamAbout, List, Gallery
from apps.contacts.models import Contacts,PageContact
from django.core.mail import send_mail
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
def index(request):
    video = models.Video.objects.latest('id')
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
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")
       
        
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
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")

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
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")
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
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")
    return render(request, 'gallery.html', locals())


def list_price(request):
    settings = models.Settings.objects.latest('id')
    list = List.objects.latest('id')
    if request.method=="POST":
            name = request.POST.get('name')
            number = request.POST.get('number')
            data = request.POST.get('data')
            contacts = Contacts.objects.create(name=name, number=number, data=data) 
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")
                
    return render(request, 'list.html', locals())

def news(request):
    settings = models.Settings.objects.latest('id')
    all_news = News.objects.all()

    paginator = Paginator(all_news, 3)  
    page = request.GET.get('page')

    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
       
        news = paginator.page(paginator.num_pages)  
    if request.method=="POST":
            name = request.POST.get('name')
            number = request.POST.get('number')
            data = request.POST.get('data')
            contacts = Contacts.objects.create(name=name, number=number, data=data) 
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")
                
    return render(request, 'news.html', locals())

def contact(request):
    settings = models.Settings.objects.latest('id')
    
    if request.method=="POST":
        if 'bron_form' in request.POST:
            name = request.POST.get('name')
            number = request.POST.get('number')
            data = request.POST.get('data')
            contacts = Contacts.objects.create(name=name, number=number, data=data) 
            if contacts:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Дата:  {data}
Номер телефона:  {number}
""")

            

        if 'contact_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            page_contact = PageContact.objects.create(name=name, email=email, number=number,  subject=subject, message=message)
            send_mail(
                f'{name}',
                f'''Здравствуйте {name},
Спасибо за обратную связь, Мы скоро свами свяжемся.
Ваша почта: {email}''',
                "noreply@somehost.local",
                [email])
            return redirect('index')
            
    return render(request, 'contact.html', locals())

def blog_news(request, id):
    settings = models.Settings.objects.latest('id')
    blog = News.objects.get(id=id)
    

    return render(request, 'post.html', locals())

 

