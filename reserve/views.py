from django.shortcuts import render,redirect
from .models import Reservation, Shelter
from .forms import UserForm,ShelterForm
from django.http import HttpResponseRedirect


def find_shelter(request):
	shelters=Shelter.objects.all()
	return render(request, 'reserve/find_shelter.html', {'shelters': shelters})

def reserve(request):
    shelter_id=request.GET.get('shelter_id')
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            reservation=Reservation(name='naghi')
            reservation.save()

            shelter = Shelter.objects.get(pk = shelter_id)
            shelter.beds_available-=1
            print shelter.beds_available
            shelter.save()

            return redirect('/')
    else:
        form = UserForm()
        shelter=Shelter.objects.filter(id = shelter_id)
    return render(request, 'reserve/reserve.html', 
        {'form': form, 'shelter':shelter})
