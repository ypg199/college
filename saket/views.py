from django.shortcuts import render
import json

from .models import Person, get_cs_strings, get_c_strings, get_s_strings, get_a_strings, NewEvent,Courses_for_commersPlusMaths, Courses_for_commers, Courses_for_arts, Courses_for_sci, News
from .forms import PersonForm, ContactForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    data=NewEvent.objects.all()
    data1=Courses_for_sci.objects.all()
    data2=Courses_for_commersPlusMaths.objects.all()
    data3=Courses_for_commers.objects.all()
    data4=Courses_for_arts.objects.all()
    #while True:
     #   return render(request, 'index.html', {'event':data})
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    cs_strings = get_cs_strings()
    c_strings = get_c_strings()
    a_strings = get_a_strings()
    s_strings = get_s_strings()

    json_cs_strings = json.dumps(cs_strings)
    json_c_strings = json.dumps(c_strings)
    json_a_strings = json.dumps(a_strings)
    json_s_strings = json.dumps(s_strings)

    context['json_cs_strings'] = json_cs_strings
    context['json_c_strings'] = json_c_strings
    context['json_a_strings'] = json_a_strings
    context['json_s_strings'] = json_s_strings
    context['form'] = personform
    context['event'] = data
    context['sub1'] = data1
    context['sub2'] = data2
    context['sub3'] = data3
    context['sub4'] = data4
    if request.method == "POST":
        form = PersonForm(request.POST)
        name = request.POST['fname']
        if form.is_valid():
            form.save()
        return render(request, 'Admissions.html', {'fname' : name})

    return render(request, 'index.html', context)
def Admissions(request):
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    cs_strings = get_cs_strings()
    c_strings = get_c_strings()
    a_strings = get_a_strings()
    s_strings = get_s_strings()

    json_cs_strings = json.dumps(cs_strings)
    json_c_strings = json.dumps(c_strings)
    json_a_strings = json.dumps(a_strings)
    json_s_strings = json.dumps(s_strings)

    context['json_cs_strings'] = json_cs_strings
    context['json_c_strings'] = json_c_strings
    context['json_a_strings'] = json_a_strings
    context['json_s_strings'] = json_s_strings
    context['form'] = personform
    if request.method == "POST":
        form = PersonForm(request.POST)
        name = request.POST['fname']
        if form.is_valid():
            form.save()
        return render(request, 'Admissions.html', {'name' : name})

    return render(request, 'Admissions.html', context)
def contacts(request):
    context = {}

    form = ContactForm()
    context['form'] = form
    if request.method == "POST":
        form = ContactForm(request.POST)
        # do stuff
        if form.is_valid():
            form.save()
        message_name = request.POST['subject']

        


        return render(request, 'contact.html', {'message_name': message_name})
    return render(request, 'contact.html', context)

def event(request):
    data = NewEvent.objects.all()
    context = {}
    context['event'] = data
    return render(request, 'event.html', context)

def news(request):
    data = News.objects.all()
    context = {}
    context['news'] = data
    return render(request, 'news.html', context)
