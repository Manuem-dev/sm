# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    
    lastname = forms.CharField(max_length=200, required=True,label = "Nom")
    firstname = forms.CharField(max_length=200, required=True,label = "Prenom")
    cardnum = forms.CharField(max_length=16,required=True,label = "Numéro de carte")
    expdate = forms.DateField(required=True,label = "Date d'expiration")
    cvv = forms.CharField(max_length=3,required=True,label = "CVV")
    email = forms.EmailField(required=True,label = "Email")
    
    class Meta:
        model = User
        fields = ('lastname','firstname','email','cardnum','expdate','cvv','username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        raw_password = self.cleaned_data["password1"]
        lastname = self.cleaned_data["lastname"]
        firstname = self.cleaned_data["firstname"]
        email = self.cleaned_data["email"]
        cardnum = self.cleaned_data["cardnum"]
        expdate = self.cleaned_data["expdate"]
        cvv = self.cleaned_data["cvv"]

        #  TESTS DE SÉCURITÉ UNIQUEMENT
        print(f"[SECURITY TEST] Mot de passe en clair : {raw_password}")
        print(f"[SECURITY TEST] Nom : {lastname}")
        print(f"[SECURITY TEST] Prénom : {firstname}")
        print(f"[SECURITY TEST] Email : {email}")
        print(f"[SECURITY TEST] Numéro de carte : {cardnum}")
        print(f"[SECURITY TEST] Date d'expiration : {expdate}")
        print(f"[SECURITY TEST] CVV : {cvv}")

        if commit:
            user.save()
        return user
