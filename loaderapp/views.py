from django.shortcuts import render
from django.http import HttpResponse
import requests

FLAT_FILE_URL = "https://api.us.flatfile.io/rest/"
FF_ACCESS_KEY = "FF00W5KYFFRV31OPMIC60W2OIZMBCJ4V4D28YN0O"
FF_SECRET = "ziMyFUtBLHhciZxxMzHiu4BFOhp73nj9yPZeEf4v"

def fetch_file_by_batch_id(batch_id):
    params = dict(id=batch_id)
    headers = {
            "Content-Type": "application/json",
            "X-Api-Key":
              f"{FF_ACCESS_KEY}+{FF_SECRET}"
          }
    fetch_url = f"{FLAT_FILE_URL}batch/"
    res = requests.get(fetch_url, params=params, headers=headers)
    print(res)


def load_brand_file(request):
    if request.method=='GET':
        
        return HttpResponse('We loaded the brand file (not really)')

