from msilib import PID_TITLE

import requests
from django.shortcuts import render

from Academy.forms import FormStudent

# Create your views here.


def Index(request, url):

    data = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=841c981cfa8c4a3696b9930cc105f5ac")

    if data.status_code == 200:
        dataJson = data.json()
        if dataJson["totalResults"] > 0:
            list = []
            for i in range(len(dataJson["articles"])):
                print(dataJson["articles"][i]["source"]["name"])

                if not dataJson["articles"][i]["source"]["name"] in list:
                    list.append(dataJson["articles"][i]["source"]["name"])
            print("")
            print(url)
            print("")

            if url != "News":
                a = 0
                for i in range(len(dataJson["articles"])):
                    print(a)
                    # print(url)
                    # print(dataJson["articles"][a]["source"]["name"])
                    if dataJson["articles"][a]["source"]["name"] != url:
                        dataJson["articles"].pop(a)

                    else:
                        print(dataJson["articles"][a]["source"]["name"])
                        a = a + 1

            for i in range(len(dataJson["articles"])):
                dataJson["articles"][i]["publishedAt"] = (
                    dataJson["articles"][i]["publishedAt"].replace("T", " ").replace("Z", "")
                )

            print(list)
            return render(request, "home.html", {"datos": dataJson["articles"], "list": list})

        else:
            print("no hay datos")

    return render(request, "home.html")


def Student(request):

    if request.method == "POST":
        datastudent = FormStudent(request.POST)
        if datastudent.is_valid:
            data = datastudent.cleaned_data
            return render(
                request,
                "enviado.html",
                {
                    "id": data["ID"],
                    "name": data["name"],
                    "phone": data["Phone"],
                },
            )
    else:

        form = FormStudent()
        return render(request, "formulario.html", {"form": form})
