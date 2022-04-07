from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from loaderapp.models import BrandThreshold, Brand
from decimal import Decimal
import traceback


class FlatFileApi:

    FLAT_FILE_URL = "https://api.us.flatfile.io/rest/"
    FF_ACCESS_KEY = "FF00W5KYFFRV31OPMIC60W2OIZMBCJ4V4D28YN0O"
    FF_SECRET = "ziMyFUtBLHhciZxxMzHiu4BFOhp73nj9yPZeEf4v"
    AUTH_TOK = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFuZ3VzbGV1bmcyMjhAaG90bWFpbC5jb20iLCJzdWIiOiIyOTYyNyIsImFjY2Vzc0tleUlkIjoiRkYwMFc1S1lGRlJWMzFPUE1JQzYwVzJPSVpNQkNKNFY0RDI4WU4wTyIsImlhdCI6MTY0OTI3NDA5NCwiZXhwIjoxNjQ5Mjc0Njk0fQ.9AE4_gI3YBeICDjFApfXWwg9WFCbNocS9CMvJMmyZuw"""  # noqa
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": f"{FF_ACCESS_KEY}+{FF_SECRET}",
        "Authorization": AUTH_TOK
    }

    def fetch_rows_by_batch_id(self, batch_id):
        fetch_url = f"{self.FLAT_FILE_URL}batch/{batch_id}/rows"
        res = requests.get(fetch_url, headers=self.headers)
        data = json.loads(res.content.decode())
        return data

    def fetch_batch_meta(self, batch_id):
        fetch_url = f"{self.FLAT_FILE_URL}batch/{batch_id}/"
        res = requests.get(fetch_url, headers=self.headers)
        data = json.loads(res.content.decode())
        return data

from django.views.decorators.csrf import csrf_exempt  # TODO: undo this
@csrf_exempt  # TODO: undo this
def load_brand_file(request):
    if request.method == 'GET':
        return HttpResponse('We loaded the brand file (not really)')
    if request.method == 'POST':
        id = request.POST['batch_id']
        dct = FlatFileApi().fetch_rows_by_batch_id(id)
        errors = list()
        successes = 0
        for d in dct['data']:
            try:
                if not d['valid']:
                    continue
                row = d['mapped']
                version = row['version']
                threshold = Decimal(row['min_threshold'])
                brand, _ = Brand.objects.get_or_create(key=row['key'], defaults={'name': row['key']})
                BrandThreshold.objects.create(version=version, min_threshold=threshold, brand=brand)
            except Exception:
                errorJson = dict(id=d['id'], batch_id=d['batchId'], row=d['sequence'], error=traceback.format_exc())
                errors.append(errorJson)
            else:
                successes += 1
        response = {'errors': errors, 'successes': f'{successes}/{dct["pagination"]["totalCount"]}'}
        return JsonResponse(response, safe=False)

