from django import forms
from survey.models import *

class CreateCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class CreateStateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'
