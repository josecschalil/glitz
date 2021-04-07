from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import Contact,activities
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
import time
# Create your views here.
def home(request):
    return render (request,'index.html')
def dashboard(request):
    if request.user.is_authenticated:
    
        if request.method =='POST':
            activity_name=request.POST.get('activity')
            Description=request.POST.get('description')
            Date=request.POST.get('date')
            list=request.POST.get('list')
            print(activity_name,Description,Date,list)
            myquery=activities(name=activity_name,description=Description,date=Date,list=list,finish=False)
            myquery.root=request.user
            myquery.save()
            return HttpResponseRedirect('/dashboard')
        admin=request.user
        data = activities.objects.filter(root=admin)
        home_set=set()
        work_set=set()
        travel_set=set()
        shopping_set=set()
        important_set=set()
        other_set=set()
        for e in data:

            if(e.list =='Home'):
                print('added to home')
                home_set.add(e)
            elif(e.list =='Important'):
                print('added to impo')
                important_set.add(e)
            elif(e.list =='Travel'):
                travel_set.add(e)
                print('added to travel')
            elif(e.list =='Work'):
                work_set.add(e)
                print('added to work')
            elif(e.list =='Shopping'):
                shopping_set.add(e)
                print('added to shopping')
                print(e.finish)
            else :
                print('added to others')
                other_set.add(e)
        homeEmpty = (len(home_set) == 0)
        workEmpty = (len(work_set) == 0)
        shoppingEmpty = (len(shopping_set) == 0)
        travelEmpty = (len(travel_set) == 0)
        impoEmpty = (len(important_set) == 0)
        othersEmpty = (len(other_set) == 0)
        context={}
        
        if  not homeEmpty:
            context['home'] = home_set
        if  not workEmpty:
            context['work'] = work_set
        if  not shoppingEmpty:
            context['shopping'] = shopping_set
        if  not travelEmpty:
            context['travel'] =travel_set
        if  not impoEmpty:
            context['important'] = important_set
        if  not othersEmpty:
            context['others'] = other_set
        return render (request,'test.html',context)

    else:
        messages.warning(request,'Please Login And Try Again')
    return render (request,'test.html')

def signin(request):
    if(request.method =='POST'):
        uname=request.POST.get('uname')
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=uname,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Success')
            return redirect('/')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('/signin')
    return render(request,'signin.html')

def signup(request):
    if(request.method =='POST'):
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        try:
            if User.objects.get(username=uname):
                messages.warning(request,'User Name is taken')
                return redirect('/signup')
        except Exception as identifier:
            pass
        try:
            if User.objects.get(email=email):
                 messages.warning(request,'E-mail Already Used')
                 return redirect('/signup')
        except Exception as identifier:
            pass
        if(pass1 != pass2):
            messages.warning(request,'Password Do not Match')
        myuser=User.objects.create_user(uname,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'SignUp Successful')
        myuser=authenticate(username=uname,password=pass1)
        login(request,myuser)
        return redirect('/')
    return render(request,'signup.html')

def signout(request):
    logout(request)
    messages.success(request,'LogOut Successful')
    return redirect('/')

def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        description=request.POST.get('desc')
        myquery=Contact(name=name,phone=phone,email=email,description=description)
        myquery.save()
        from_mail =settings.EMAIL_HOST_USER
        connection= mail.get_connection()
        connection.open()
        email_message =mail.EmailMessage(f'Email From {name} ',f'Email From: {name}\n Phone Number: {phone} \n email: {email}\n Content: {description}',from_mail,['josecschalil@gmail.com'],connection=connection)
        email_message_client =mail.EmailMessage(f'Website Response',f'Dear {name}\n\n Thanks for Contacting Us. We Will get back to you soon...',from_mail,[email],connection=connection)
        connection.send_messages([email_message,email_message_client])
        connection.close()
        messages.info(request,'Your Response Has Been Submitted')
        return HttpResponseRedirect('/contact')
        
    return render(request,'contact.html')

def dashboards(request):
    
    if request.method =='POST':
        user_id=request.POST.get('ids')
        print(user_id)
        a = activities.objects.filter( id=user_id)
        a.delete()
        return HttpResponseRedirect('/dashboard')

def finishbutton(request):
    
    if request.method =='POST':
        user_id=request.POST.get('setfinish')
        print(user_id)
        a = activities.objects.get( id=user_id)
        a.finish =(True)
        a.save()
        return HttpResponseRedirect('/dashboard')


def editbutton(request):
    
    if request.method =='POST':
        tableid=request.POST.get('tableid')
        activity_name=request.POST.get('activity')
        Description=request.POST.get('description')
        Date=request.POST.get('date')
        list=request.POST.get('list')
        print(activity_name,Description,Date,list)
        a = activities.objects.get( id=tableid)
        a.name=(activity_name)
        a.description=(Description)
        a.date=(Date)
        a.list=(list)
        a.finish=(False)
        a.save()
        return HttpResponseRedirect('/dashboard')

def about(request):
    return render(request, 'about.html')
        

    
