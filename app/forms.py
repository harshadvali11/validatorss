from django import forms


def check_for_a(value):
    if value[0].lower()!='a':
        raise forms.ValidationError('Name Should start with a')



class Student(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])