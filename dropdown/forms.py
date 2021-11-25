from django import forms

from .models import Person,Country,state,city


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = state.objects.all()

        if 'Country' in self.data:
            try:
                Country_id = int(self.data.get('Country'))
                self.fields['state'].queryset = state.objects.filter(Country_id=Country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
      #  elif self.instance.pk:
          #  self.fields['state'].queryset = self.instance.Country.state_set.order_by('name')