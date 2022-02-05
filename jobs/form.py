from django import forms

from .models import applicant , job




class ApplyForm(forms.ModelForm): #make form from existing model
    class Meta:
        model = applicant
        fields = ['national_id' ,'name','email','biography','experience_level','Programming_language']


class AddForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('slug','owner')
        