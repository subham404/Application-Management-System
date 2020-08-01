from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone

from django.contrib.auth import login as auth_login

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ApplicationForm,RegisterForm
from .models import Application,Register
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from django.contrib.auth import logout
from django.utils.decorators import method_decorator

class AboutView(TemplateView):
    template_name='home.html'

@login_required
def student_view(request):
    app=Application.objects.filter(schId=request.user.schId).order_by('-created_on')
    return render(request,'apply.html',{'app_list':app})

def detect(request):
    info=request.user.schId
    request.user.is_hod=True
    if info==10015:
        return 'hod_cse'
    elif info==10011:
        return 'hod_ce'
    elif info==10012:
        return 'hod_ee'
    elif info==10013:
        return 'hod_me'
    elif info==10014:
        return 'hod_ece'
    elif info==10016:
        return 'hod_ei'
    else:
        request.user.is_hod=False
        return ''
    
    
def RegisterView(request):
    if request.user.is_authenticated:
        x=detect(request)
        if len(x)==0:
            return redirect('apply')
        else:
           
            return redirect(x)
        
        
    else:
        form= RegisterForm()
        if request.method=='POST':
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('name')
                messages.success(request, 'Account was created for ' + user)
                
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)

def authenticate(request,schId,password):
    user=Register.objects.get(schId=schId)
    if user is None:
        return None
    if user.password==Register.objects.get(schId=schId).password:
        return user
    return None
    
def LoginView(request):
    if request.user.is_authenticated:
        x=detect(request)
        if len(x)==0:
            return redirect('apply')
        else:
            return redirect(x)
    else:
        if request.method=='POST':
            schId=request.POST['schId']
            password =request.POST['password']
            
            user = authenticate(request,schId,password)
            
            
            if user is not None:
                auth_login(request,user)
                x=detect(request)
                if len(x)==0:
                    return redirect('apply')
                else:
                    return redirect(x)
            else:
                messages.info(request, 'Incorrect id or password')
                
        context = {}
        return render(request, 'login.html', context)




def approve_application(request,pk):
    application=get_object_or_404(Application,pk=pk)
    application.approve()
    branch=application.branch
    if branch=='CSE':
        return redirect('hod_cse')
    elif branch=='CE':
        return redirect('hod_ce')
    elif branch=='EE':
        return redirect('hod_ce')
    elif branch=="ME":
        return redirect('hod_me')
    elif branch=='EI':
        return redirect('hod_ei')
    else:
        return redirect('hod_ece')
    
def reject_application(request,pk):
    application=get_object_or_404(Application,pk=pk)
    branch=application.branch
    application.delete()
    if branch=='CSE':
        return redirect('hod_cse')
    elif branch=='CE':
        return redirect('hod_ce')
    elif branch=='EE':
        return redirect('hod_ce')
    elif branch=="ME":
        return redirect('hod_me')
    elif branch=='EI':
        return redirect('hod_ei')
    else:
        return redirect('hod_ece')
    
class ApplicationView(CreateView,LoginRequiredMixin):
    model=Application
    form_class=ApplicationForm
    template_name='application.html'
    redirect_field_name='apply.html'
    
class ApplicationDetailView(DetailView):
    model=Application
    
def CSEApplication(request):
    app=Application.objects.filter(branch=request.user.branch).order_by('-created_on')
    return render(request,'hod_cse.html',{'hod_cse':app})

def CEApplication(request):
    app=Application.objects.filter(branch=request.user.branch).exclude(approved=True).order_by('-created_on')
    return render(request,'hod_ce.html',{'hod_ce':app})
    
def ECEApplication(request):
    app=Application.objects.filter(branch=request.user.branch).order_by('-created_on')
    return render(request,'hod_ece.html',{'hod_ece':app})
    
def EEApplication(request):
    app=Application.objects.filter(branch=request.user.branch).order_by('-created_on')
    return render(request,'hod_ee.html',{'hod_ee':app})
    
def MEApplication(request):
    app=Application.objects.filter(branch=request.user.branch).order_by('-created_on')
    return render(request,'hod_me.html',{'hod_me':app})
    
def EIApplication(request):
    app=Application.objects.filter(branch=request.user.branch).exclude(approved=True).order_by('-created_on')
    return render(request,'hod_ei.html',{'hod_ei':app})
    
    
    
    
    
    
    
    
    
    
    
    
    