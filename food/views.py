# food/views.py
from django.shortcuts import render, redirect
from ftplib import FTP
# from django.shortcuts import render
# import pandas as pd
import matplotlib.pyplot as plt
# from io import BytesIO
# import base64

def uploadData():
#
    # ftp = FTP("192.168.10.211", timeout=120)
    ftp = FTP("93.33.192.68", timeout=120)

    ftp.login('ftpdaticentzilio', 'Sd2PqAS.We8zBK')
    ftp.cwd('/dati/ponte_giurino')

    gFile = open('PGDailyPlot.csv', "wb")
    ftp.retrbinary('RETR PGDailyPlot.csv', gFile.write)
    gFile.close()

    # Data = pd.read_csv("PGDailyPlot.csv")
    Data = 0
    return Data


def index2(request):
    stepcount = [
        {"y": 10560, "label": "Sunday"},
        {"y": 9060, "label": "Monday"},
        {"y": 6650, "label": "Tuesday"},
        {"y": 8305, "label": "Wednesday"},
        {"y": 8531, "label": "Thursday"},
        {"y": 10150, "label": "Friday"},
        {"y": 8921, "label": "Saturday"}
    ]

    return render(request, 'index2.html', {"stepcount": stepcount})

def index(request):

    Data = uploadData()

    # t = pd.to_datetime(Data["t"])
    # Q = Data["Q"]
    #
    # fig, ax = plt.subplots()
    #
    # ax.plot(t, Q, lw=1.5, label="Potenza [kW]", color="red")

    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_png = buffer.getvalue()
    # buffer.close()

    # graphic = base64.b64encode(image_png)
    # graphic = graphic.decode('utf-8')
    Data = {"Data":"Ciao"}

    # return render(request, 'index.html', {'graphic': graphic})
    return render(request, 'index.html', context=Data)


# Create your views here.
