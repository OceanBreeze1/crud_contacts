from django.shortcuts import render
from django.shortcuts import render, redirect

from apps.forms import UserForm
from apps.models import User


def home(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'app/index.html', context)


def add_person(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'app/add.html')


def update_person(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'user': user}
    return render(request, 'app/edit.html', context)


def delete_person(request, pk):
    user = User.objects.filter(id=pk)
    user.delete()
    return redirect('/')


# Create your views here.
