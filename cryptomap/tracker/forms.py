from django import forms


class AddNewItemForm(forms.Form):
    requested_price = forms.IntegerField()