
from django import forms
from .models import Travel

class NewTravel(forms.ModelForm):

    class Meta:
        model = Travel
        fields =('Name','Phonenumber','CarNumber','DateOfRegister','AutoModel','Description','NumOfSits','Start','Destonation','Price')

class TravelParameters(forms.ModelForm):

    class Meta:
        model = Travel
        fields = ('Start','Destonation')

#class TravelParameters(forms.Form):
#    
#    s = forms.CharField(label='Пункт отправки',max_length=100)
#    d = forms.CharField(label='Пункт прибытия',max_length=100)