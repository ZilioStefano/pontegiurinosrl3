# food/views.py
from django.shortcuts import render, redirect
from ftplib import FTP

def index(request):

    ftp = FTP("93.33.192.68", timeout=120)  # Cartella Centrali
    return render(request, 'index.html', context=None)


# Create your views here.
