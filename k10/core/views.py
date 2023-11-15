from item.models import *
from center.models import *
from .forms import *
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    return render(request, 'core/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['name']
            fdoctor = form.cleaned_data['doctor']
            subject = "Запись на прием"
            message = f"{fname}, Вы добавлены на эту неделю в живую очередь к специалисту {fdoctor}.\nЖдём Вас в оздоровительном центре Басманный двор!"
            try:
                send_mail(subject, message, 'basmannyjdvor@gmail.com', [form.cleaned_data['email'] ])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/center/")

    form = ContactForm()
    return render(request, "core/contact.html", {'form': form})


def aboutmuseum(request):
    return render(request, 'core/aboutmuseum.html')


def eventsmuseum(request):
    events = MEvent.objects.all()
    return render(request, 'core/eventsmuseum.html', {
        'events': events
    })

def museum(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/museum.html', {
        'categories': categories,
        'items': items
    })

def museumcategory(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/museum.html', {
        'categories': categories,
        'items': items
    })


def aboutcenter(request):
    return render(request, 'core/aboutcenter.html')


def eventscenter(request):
    events = CEvent.objects.all()
    return render(request, 'core/eventscenter.html', {
        'events': events
    })


def center(request):
    doctors = Doctor.objects.all()
    specializations = Specialization.objects.all()
    return render(request, 'core/center.html', {
        'specializations': specializations,
        'doctors': doctors
    })

