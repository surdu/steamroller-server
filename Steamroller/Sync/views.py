import json
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError


def setData(request):
    try:
        data = request.POST["data"]
        with open("syncData.json", "w") as f:
            f.write(data.encode("utf-8"))

    except IOError:
        return HttpResponse(json.dumps({"status": "error", "details": "Could not open sync file"}), status=500)

    except MultiValueDictKeyError:
        return HttpResponse(json.dumps({"status": "error", "details": "Data not found"}), status=400)

    return HttpResponse(json.dumps({"status": "ok"}))


def getData(request):
    try:
        with open("syncData.json", "r") as f:
            data = f.read()
    except IOError:
        return HttpResponse(json.dumps({"status": "ok", "data": json.dumps({"watchedItems": {}, "boughtItems": []})}))

    return HttpResponse(json.dumps({"status": "ok", "data": data}))
