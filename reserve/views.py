from django.shortcuts import render,redirect
from .models import User,Shelter
from .forms import UserForm,ShelterForm
from django.http import HttpResponseRedirect


def find_shelter(request):
	shelters=Shelter.objects.all()
	return render(request, 'reserve/find_shelter.html', {'shelters': shelters})

def reserve(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    shelter_id=request.GET['shelter_id']
    shelter=Shelter.objects.filter(id=shelter_id)

    return render(request, 'reserve/reserve.html', {'form': form,'shelter':shelter})
