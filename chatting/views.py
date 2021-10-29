from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    texts = Text.objects.all()
    form = TextForm()

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'index.html', {'texts': texts, 'form':form})