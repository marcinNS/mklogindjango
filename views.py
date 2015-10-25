from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.forms.util import ValidationError
from django.core.mail import send_mail
#from django.forms.formsets import formset_factory

from . models import MyUser
from . forms import MyUserForm

def index(request):
    context=''
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def profile(request):
    SEX = {0:"M",1:"F"}
    msg=''
    user = get_object_or_404(User, pk=request.user.pk)
    #UserFormSet = formset_factory(MyUserForm)
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            # do something with the formset.cleaned_data
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.set_password(form.cleaned_data['password'])
            user.save()
            myuser, created = MyUser.objects.get_or_create(pk=user.myuser.id)
            myuser.wiek = form.cleaned_data['wiek']
            myuser.sex = form.cleaned_data['sex']
            myuser.miasto = form.cleaned_data['miasto']
            myuser.kategoria = form.cleaned_data['kategoria']
            myuser.save()
            msg='Twoje dane zostały zapisane'
    else:
        form = MyUserForm(initial={
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'wiek':user.myuser.wiek,
            'sex':user.myuser.sex,
            'miasto':user.myuser.miasto,
            'kategoria':[k.id for k in user.myuser.kategoria.all()],
            'rejestracja':False
            })
    context = {'form':form, 'msg':msg}
    return render(request, 'account/profile.html', context)
    
def register(request):
    import random
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid(): #and form.cleaned_data['password']==form.cleaned_data['password1']
            password1=form.cleaned_data['password']
            user = User.objects.create_user(username = form.cleaned_data['email'].replace('@',''), password=password1)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.is_active = False
            user.save()
            myuser = MyUser.objects.create(user_id=user.id, activationcode=int(random.random()*1000000))
            myuser.wiek = form.cleaned_data['wiek']
            myuser.sex = form.cleaned_data['sex']
            myuser.miasto = form.cleaned_data['miasto']
            myuser.kategoria = form.cleaned_data['kategoria']
            myuser.save()
            # redirect to a new URL:
            
            msg = 'Prosimy aktywować adres e-mail klikając na ten link http://vps151689.ovh.net:8000/newlogin/activate/'+str(myuser.activationcode)+'/'
            send_mail('Aktywacja konta serwisu', msg, 'from@example.com',[user.email], fail_silently=True)
            return HttpResponseRedirect('/newlogin/')
    else:
        form = MyUserForm(initial={'rejestracja':True})
    context = {'form':form}
    return render(request, 'registration/register.html', context)

def activate(request,kod):
    try:
        profil=MyUser.objects.get(activationcode=kod)
        user = User.objects.get(pk=profil.user.id)
        user.is_active=True
        user.save()
    except:
        msg="Coś poszło nie tak"
        pass
    return render(request, 'registration/activate.html')
    
class UserView(generic.DetailView):
    model = MyUser
    template_name = 'account/profile.html'