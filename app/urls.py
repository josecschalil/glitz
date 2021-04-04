from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('dashboard/edit',views.editbutton,name='editbutton'),
    path('dashboard/finish',views.finishbutton,name='finishbutton'),
    path('dashboard/test',views.dashboards,name='dashboards'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),


]
