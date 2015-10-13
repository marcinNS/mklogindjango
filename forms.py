from django import forms
from django.forms import ModelForm,PasswordInput,HiddenInput
from django.contrib.auth.models import User
from . models import MyUser,Kategoria

'''
class MyUserForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['user','wiek','sex','miasto','kategoria']
'''
        
class MyUserForm(forms.Form):
    SEX = [
        ("M","Mężczyzna"),
        ("F","Kobieta")
    ]
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label="Hasło",widget=PasswordInput())
    password1 = forms.CharField(label='Potwierdź hasło',widget=PasswordInput())
    first_name = forms.CharField(label='Imię', max_length=100)
    last_name = forms.CharField(label='Nazwisko', max_length=100)
    wiek = forms.DateField(label='Dzień urodzin',required=False)
    sex = forms.ChoiceField(label='Płeć', choices=SEX,required=False)
    miasto = forms.CharField(label='Miasto', max_length=100,required=False)
    kategoria = forms.ModelMultipleChoiceField(label='Kategorie', queryset=Kategoria.objects.all(),required=False)
    rejestracja = forms.BooleanField(widget=HiddenInput(),required=False)
    
    def clean(self):
        cleaned_data = super(MyUserForm, self).clean()
        if cleaned_data.get('rejestracja'):
            email=cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Podany email istnieje w bazie.")
        password1=cleaned_data.get('password')
        password2=cleaned_data.get('password1')
        if password1 and password1 != password2:
            raise forms.ValidationError("Hasła do siebie nie pasują.")
        return cleaned_data