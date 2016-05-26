from django import forms
from .models import Reservation, Shelter, User


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('shelter_name','person_name','person_phone')

class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ('name','phone','address')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','phone')
