from django import forms
from app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','contact','email','password']
        labels = {'name':'NAME','password':'PASSWORD','contact':'CONTACT','email':'EMAIL'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter Name','autofocus':True,'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'placeholder':'Enter Email','class':'form-control'}),
                   'password':forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'p','class':'form-control'}),
                   'contact':forms.NumberInput(attrs = {'placeholder':'enter mobile no','class':'form-control'})}
