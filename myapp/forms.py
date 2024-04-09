from django import forms
from .models import Candidates,Organizations

class CandidateRegistrationForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ['name', 'email', 'phone_number', 'city', 'address',
                  'tenth_school', 'tenth_year', 'tenth_marks',
                  'twelfth_school', 'twelfth_year', 'twelfth_marks',
                  'skill1', 'skill2', 'skill3', 'interested_position']

class OrgRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Organizations
        fields = ['name', 'email', 'password']

class OrgLoginForm(forms.Form):
    email=forms.EmailField(label='Email')
    password=forms.CharField(label='password',widget=forms.PasswordInput)