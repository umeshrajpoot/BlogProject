from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Blog_Post,BlogPost

class user_form(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.TextInput(attrs={'class':'form-control'})
                 }
        
# class login_form(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Change the class name of the username field
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         # Change the class name of the password field
#         self.fields['password'].widget.attrs.update({'class': 'form-control'})
        
#also use login form this type and also use upper type method

class login_form(AuthenticationForm):
    username =UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password =forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete':'current-password'}))


class Addpost_form(forms.ModelForm):
    class Meta:
        model=Blog_Post
        fields=['id','title','desc']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'desc':forms.Textarea(attrs={'class':'form-control'})}
        
class Add_post_form(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['id','username','title','desc']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'desc':forms.Textarea(attrs={'class':'form-control'}),
                 'username':forms.TextInput(attrs={'class':'form-control'}
                    
                 )}