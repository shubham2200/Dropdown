from django import forms

from .models import Person,Country,state,city


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


  