from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import sentiment_analysis as st
from . utils import get_plot



# Create your views here.

def index(request):

    if request.method == "POST":
        text = request.POST.get("text")
        number = request.POST.get("number")
        print(text , number)

        FullData = st.analysis(text,number)


        data = FullData["data"]
        label = FullData["label"]
        value = FullData["val"]
        accuracy = FullData["accuracy"]

        chart = get_plot(data=data , labels=label)

        context = {
            "chart":chart,
            "value":value,
            "accuracy":accuracy
        }
        return render(request,"sentimental/index.html" , context)

    return render(request,"sentimental/index.html")