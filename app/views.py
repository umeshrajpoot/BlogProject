from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .form import user_form,login_form,Addpost_form,Add_post_form
from django.contrib import messages
from .models import Blog_Post,BlogPost
from django.http import HttpResponse
from django.contrib.auth.models import Group

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import DeleteView

# Create your views here.
def Home(request):
    data=BlogPost.objects.all()
    
    return render(request,'app/home.html',{'data':data})

def About(request):
    return render(request,'app/about.html')

def Contact(request):
    return render(request,'app/contact.html')

def Signup(request):
    if request.method=='POST':
        form=user_form(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            messages.success(request,'you have successfully registered as Author..')
            form=user_form()
        else:
            messages.warning(request,'please fill all the correct detail....')
    else:
        form=user_form()
    return render(request,'app/signup.html',{'form':form})

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=login_form(request,request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                passw=form.cleaned_data['password']
                user=authenticate(request,username=uname,password=passw)
                if user is not None:
                    login(request,user)
                    messages.success(request,'user login successfully... ')
                    return redirect('/deshboard/')
        else:
            form=login_form()
        return render(request,'app/login.html',{'form':form})
    else:
        return redirect('/deshboard/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        messages.info(request,'you are not a logged in so please login first...')
        return redirect('/login/')
    

def Deshboard(request):
    if request.user.is_authenticated:
        usr1=User.objects.filter(is_staff=True,username=request.user)
        if usr1:
            data=BlogPost.objects.all()
            user=request.user
            fullname=user.get_full_name()
            gps=user.groups.all()
            print("yes",usr1)
            param={'data':data,
                'fullname':fullname,
                'gps':gps,
                'usr':user}
        else:

            usr=User.objects.filter(username=request.user)
            for u in usr:
                uname=u.username
            data=BlogPost.objects.filter(username=uname)
            user=request.user
            fullname=user.get_full_name()
            gps=user.groups.all()
            print("no")
            param={'data':data,
                'fullname':fullname,
                'gps':gps,
                'usr':user}
        return render(request,'app/deshboard.html',param)
    else:
        return redirect('/login/')
    
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.user
            form=Add_post_form(request.POST,initial={'username':name})
            if form.is_valid():
                form.save()
                messages.success(request,'your post successfully add...')
                form=Add_post_form(initial={'username':name})
        else:
            name=request.user
            form=Add_post_form(initial={'username':name})
        return render(request,'app/addpost.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')
    
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            dt=BlogPost.objects.get(id=id)
            
            form =Add_post_form(request.POST,instance=dt)
            if form.is_valid():
                form.save()
                messages.success(request,'your post successfully update...')
                form=Add_post_form()
        else:
            dt=BlogPost.objects.get(id=id)
            form=Add_post_form(instance=dt)
        return render(request,'app/updatepost.html',{'form':form})

    else:
        return HttpResponseRedirect('/login/')
    
def delete_post(request,id):
    if request.user.is_authenticated:
        dt=BlogPost.objects.get(id=id)
        dt.delete()
        messages.success(request,'your post successfully delete..')
        return HttpResponseRedirect('/deshboard/')
       
    else:
        return HttpResponseRedirect('/login/')
    
# class BlogPostDeleteView(PermissionRequiredMixin, DeleteView):
#     model = BlogPost
#     template_name = 'deshboard.html'
#     success_url = '/login/'
#     permission_required = 'app.delete_blog_post'

def Index(request):
    return render(request ,"app/index.html")