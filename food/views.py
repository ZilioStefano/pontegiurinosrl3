# food/views.py
from django.shortcuts import render, redirect
from ftplib import FTP
import pandas as pd


def uploadData():

    # ftp = FTP("192.168.10.211", timeout=120)
    ftp = FTP("93.33.192.68", timeout=120)

    ftp.login('ftpdaticentzilio', 'Sd2PqAS.We8zBK')
    ftp.cwd('/dati/ponte_giurino')

    gFile = open('PGDailyPlot.csv', "wb")
    ftp.retrbinary('RETR PGDailyPlot.csv', gFile.write)
    gFile.close()

    Data = pd.read_csv("PGDailyPlot.csv")
    # Data = 0
    return Data



def index(request):



    Data = uploadData()

    t = pd.to_datetime(Data["t"])
    Q = Data["Q"]
    Grafico = Data.plot(kind = "scatter", x = "t", y ="Q")

    return render(request, 'index.html', context=None)


# Create your views here.
