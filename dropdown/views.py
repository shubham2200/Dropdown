from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

from dropdown.models import Person

from .forms import PersonCreationForm
# Create your views here.

def home(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'userr is is saved successfully... ')
            return render(request, 'home.html')
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html', {'form': form})

def user_D(request):
    person = Person.objects.all()
    print(person)
    return render(request,'user_D.html',{'persons':person})