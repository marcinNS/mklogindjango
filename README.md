# mklogindjango
Extends UserModel in Django

Modules add few new field to User Model. It creates profile Class with:
- sex
- city
- dateofbirth
- category

And add Category Model to store category of some kind of items (e.g. category for lessons)

## installation
Installation is very simple process. You have to add settings.py
```
INSTALLED_APPS = (
    ...
    'mklogin',
)
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend','mklogin.models.MyBackend')
```
and to project urls.py
```
from django.contrib.auth import views
url('^newlogin/', include('mklogin.urls')),
    url(r'^password_reset/$',views.password_reset,
                    {'template_name': 'registration/password_reset_form2.html'},
                       name='auth_password_reset'),
    url(r'^password_reset/done/$',views.password_reset_done,
                    {'template_name': 'registration/password_reset_done2.html'},
                       name='auth_password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, 
                    {'template_name':'registration/password_reset_confirm2.html'}),
    url(r'^reset/done/$', views.password_reset_complete, 
                    {'template_name':'registration/password_reset_complete2.html'}),
```
If you don't have a standard url auth yet, You have to also add this line to urlspattern
'''
url('^', include('django.contrib.auth.urls'))
'''
