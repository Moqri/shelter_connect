from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm
from django.http import HttpResponseRedirect


def reserve(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'reserve/reserve.html', {'form': form})
