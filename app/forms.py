from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError('Name Should start with a')



class Student(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(4)])
    email=forms.EmailField(max_length=100)
    reenter_email=forms.EmailField(max_length=100)
    phone=forms.CharField(min_length=10,max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean_botcatcher(self):
        bot=self.cleaned_data.get('botcatcher')
        if len(bot)>0:
            raise forms.ValidationError('Bot has catched')
    
    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data.get('reenter_email')

        if e!=r:
            raise forms.ValidationError('Emails Are Not matched')
