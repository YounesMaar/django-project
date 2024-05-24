from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Depense, Budget

class CustomerUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label ="password",
        strip =False,
        widget =forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label ="password confirmation",
        widget =forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip =False,
    )

    class Meta(UserCreationForm.Meta):  
        fields = UserCreationForm.Meta.fields + ("password1", "password2")


  

class DepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ['categorie', 'montant', 'date', 'payment_method']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['categorie', 'montant', 'date']
