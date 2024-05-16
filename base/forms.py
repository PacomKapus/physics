from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, TextInput, ModelForm,PasswordInput
from django.contrib.auth.models import User
from .models import UploadedFile , UploadedFile2 , UploadedFile3 , UploadedFile4 , UploadedFile5 , Comment


class SignUpForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}), label=False)
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}), label=False)
    password1 = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}), label=False)
    password2 = CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}), label=False)
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
              
class UploadFileForm(ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file'] 

class UploadFileForm2(ModelForm):
    class Meta:
        model = UploadedFile2
        fields = ['file']

class UploadFileForm3(ModelForm):
    class Meta:
        model = UploadedFile3
        fields = ['file']

class UploadFileForm4(ModelForm):
    class Meta:
        model = UploadedFile4
        fields = ['file']

class UploadFileForm5(ModelForm):
    class Meta:
        model = UploadedFile5
        fields = ['file']
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']