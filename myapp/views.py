from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from .forms import ExtendedRegisterForm, ExtendedUpdateProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

# Register View
def signupView(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form_data = ExtendedRegisterForm(req.POST)
            if form_data.is_valid():
                form_data.save()
                form_data = ExtendedRegisterForm()
        else:
            form_data = ExtendedRegisterForm()
    else:
        return HttpResponseRedirect('/profile/')
    context = {
        'uform':form_data
    }
    return render(req,template_name='myapp/signup.html',context=context)

# Login View
def loginView(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form_data = AuthenticationForm(request=req, data=req.POST)
            if form_data.is_valid():
                uname = form_data.cleaned_data['username']
                upass = form_data.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(req,user)
                    return HttpResponseRedirect('/profile/')
        else:
            form_data = AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile/')
    context = {
        'uform' : form_data
    }
    return render(req, template_name='myapp/login.html', context=context)

# Profile View
def profile(req):
    if req.user.is_authenticated:
     return render(req, template_name='myapp/profile.html')
    else:
        return HttpResponseRedirect('/login/')

# Logout View
def logoutView(req):
    logout(req)
    return HttpResponseRedirect('/login/')

# Change password with old password
def changepass1(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form_data = PasswordChangeForm(user=req.user, data=req.POST)
            if form_data.is_valid():
                form_data.save()
                update_session_auth_hash(req,form_data.user)
                return HttpResponseRedirect('/profile/')
        else:
            form_data = PasswordChangeForm(user=req.user)
    else:
        return HttpResponseRedirect('/login')
    context = {
        'uform' : form_data
    }
    return render(req, template_name='myapp/changepassword1.html', context=context)

# Change password without old password
def changepass2(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form_data = SetPasswordForm(user=req.user, data=req.POST)
            if form_data.is_valid():
                form_data.save()
                update_session_auth_hash(req,form_data.user)
                return HttpResponseRedirect('/profile/')
        else:
            form_data = SetPasswordForm(user=req.user)
    else:
        return HttpResponseRedirect('/login/')
    context = {
        'uform' : form_data
    }
    return render(req, template_name='myapp/changepassword2.html', context=context)

# Update Profile
def updateprofile(req):
    if req.user.is_authenticated:
        if req.method == "POST":
            form_data = ExtendedUpdateProfileForm(req.POST,instance=req.user)
            if form_data.is_valid():
                form_data.save()
                return HttpResponseRedirect('/profile/')
        else:
            form_data = ExtendedUpdateProfileForm(instance=req.user)
        context = {
            'uform':form_data
        }
        return render(req,template_name='myapp/updateprofile.html',context=context)
    else:
        return HttpResponseRedirect('/login/')