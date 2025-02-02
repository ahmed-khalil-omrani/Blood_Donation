from django.shortcuts import render ,redirect, get_object_or_404
from .models import BloodDonor , BloodNeeder
from .form import DonorForm, UserForm , NeederForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
def connection(request):
    return render(request , "connection.html")


#-------------------------------------------Donor----------------------------------------------
def donor_profile(request , username):
    donor=get_object_or_404(BloodDonor , user__username=username)
    return render(request , 'donor_profile.html',{'donor':donor})


def donor_create(request):
    if request.method=='POST':
        uform=UserForm(request.POST)
        dform=DonorForm(request.POST)
        if dform.is_valid() and uform.is_valid():
           user=uform.save()
           donor=dform.save(commit=False)
           donor.user=user 
           donor.save()
           return redirect('donor_profile' , username=user.username)
    else:
        
        dform=DonorForm()
        uform=UserForm()
    return render(request , 'donor_form.html',{'dform':dform , 'uform':uform})




def login_donor(request):
    form=AuthenticationForm(data=request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            user=authenticate(request , username=form.cleaned_data['username'] , password=form.cleaned_data['password'])
            if user is not None:
                login(request , user)
                return redirect('donor_profile' , username=user.username)
    return render(request , 'login_donor.html',{'form':form} )




#--------------------------------------------Needer--------------------------------------------
def needer_profile(request , username):
    needer=get_object_or_404(BloodNeeder , user__username=username)
    return render(request , "needer_profile.html" , {'needer':needer})

def needer_create(request):
    if request.method=='POST':
        uform=UserForm(request.POST)
        nform=NeederForm(request.POST)
        if uform.is_valid() and nform.is_valid():
            user=uform.save()
            needer=nform.save(commit=False)
            needer.user=user
            needer.save()
            return redirect('needer_profile' , username=user.username)
    else:
        nform=NeederForm()
        uform=UserForm()
    return render(request , 'needer_form.html' , {'nform':nform , 'uform':uform})
        

        

# Create your views here.
