from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json

FLAT_FILE_URL = "https://api.us.flatfile.io/rest/"
FF_ACCESS_KEY = "FF00W5KYFFRV31OPMIC60W2OIZMBCJ4V4D28YN0O"
FF_SECRET = "ziMyFUtBLHhciZxxMzHiu4BFOhp73nj9yPZeEf4v"
AUTH_TOK = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFuZ3VzbGV1bmcyMjhAaG90bWFpbC5jb20iLCJzdWIiOiIyOTYyNyIsImFjY2Vzc0tleUlkIjoiRkYwMFc1S1lGRlJWMzFPUE1JQzYwVzJPSVpNQkNKNFY0RDI4WU4wTyIsImlhdCI6MTY0OTI3NDA5NCwiZXhwIjoxNjQ5Mjc0Njk0fQ.9AE4_gI3YBeICDjFApfXWwg9WFCbNocS9CMvJMmyZuw"""

def fetch_rows_by_batch_id(batch_id):
    params = dict(id=batch_id)
    headers = {
            "Content-Type": "application/json",
            "X-Api-Key": f"{FF_ACCESS_KEY}+{FF_SECRET}",
            "Authorization": AUTH_TOK
          }
    fetch_url = f"{FLAT_FILE_URL}batch/{batch_id}/rows"
    res = requests.get(fetch_url, headers=headers)
    dct = res.content.decode()
    return dct

from django.views.decorators.csrf import csrf_exempt  # TODO: undo this
@csrf_exempt  # TODO: undo this
def load_brand_file(request):
    if request.method == 'GET':
        return HttpResponse('We loaded the brand file (not really)')
    if request.method == 'POST':
        id = request.POST['batch_id']
        filejson = fetch_rows_by_batch_id(id)
        return JsonResponse(json.loads(filejson), safe=False)

