from django import forms


class PageRequestForm(forms.Form):
    description = forms.CharField(label="Номер главы", max_length=1024)