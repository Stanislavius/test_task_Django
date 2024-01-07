from django.shortcuts import render

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameValueForm
from .models import Measurement

def index(request):
    if request.method == "POST":
        form = NameValueForm(request.POST)
        if form.is_valid():
            value = request.POST['value']
            byWho = request.POST['name']
            record = Measurement(value = value, byWho = byWho)
            record.save()
            return HttpResponse("Done. Your input is saved!")
    else:
        form = NameValueForm()
        return render(request, "NameValue.html", {"form":form})
    
def show_all(request):
    MODEL_HEADERS=[f.name for f in Measurement._meta.get_fields()]
    query_results = [list(i.values()) for i in list(Measurement.objects.all().values())]
    return render(request, "Measurement_show.html", {
            "query_results" : query_results,
            "model_headers" : MODEL_HEADERS
        })
    return HttpResponse(s)

def show(request):
    inx = request.GET['id']
    obj = Measurement.objects.get(id = inx)
    return HttpResponse(str(obj.id) + " " + str(obj.date) + " " + str(obj.byWho) + " " + str(obj.value))
