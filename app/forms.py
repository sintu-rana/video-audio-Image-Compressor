from django import forms
from .models import SaveFile

class SaveFileForm(forms.ModelForm):
    class Meta:
        model=SaveFile
        # fields =('image','name','mobile','email','address')
        fields = '__all__'
