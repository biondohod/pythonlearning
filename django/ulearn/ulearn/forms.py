from django import forms
 
class AddPersonForm(forms.Form):
    fname = forms.CharField(label="Имя", max_length=64)
    lname = forms.CharField(label="Фамилия", max_length=64)
    age = forms.IntegerField(label="Возраст")
    job = forms.CharField(label="Должность", max_length=64)