from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'profile/$',views.profile),
    #url(r'profil/$',views.UserView.as_view()),
    url(r'register/$',views.register),
    #url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', {'template_name':'userpanel/password_reset_form.html', 'email_template_name':'userpanel/password_reset_email.html'}),
]