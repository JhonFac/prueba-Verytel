from django import forms


class FormStudent(forms.Form):

    ID = forms.IntegerField(required=True)
    name = forms.CharField()
    Phone = forms.IntegerField()
