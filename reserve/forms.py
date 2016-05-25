from django import forms
from .models import Reservation, Shelter, User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date','shelter','user')

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ('name','phone','address')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','phone')
