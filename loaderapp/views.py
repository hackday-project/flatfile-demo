from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json
from loaderapp.models import BrandThreshold, Brand, CategoryTree, Item
from decimal import Decimal
import traceback
import jwt


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

    def _make_get_call(self,url, **kwargs):
        res = requests.get(url, headers=self.headers, **kwargs)
        data = res.content.decode()
        data = json.loads(data)
        return data

    def fetch_rows_by_batch_id(self, batch_id):
        fetch_url = f"{self.FLAT_FILE_URL}batch/{batch_id}/rows"
        return self._make_get_call(fetch_url)

    def fetch_batch_meta(self, batch_id):
        fetch_url = f"{self.FLAT_FILE_URL}batch/{batch_id}/"
        return self._make_get_call(fetch_url)

from django.views.decorators.csrf import csrf_exempt  # TODO: undo this
@csrf_exempt  # TODO: undo this
def load_brand_file(request):
    if request.method == 'GET':
        return JsonResponse({'success':True}, safe=False)
    id = json.loads(request.body)['batch_id']
    dct = FlatFileApi().fetch_rows_by_batch_id(id)
    errors = list()
    successes = 0
    for d in dct['data']:
        try:
            row = d['mapped']
            version = row['version']
            threshold = Decimal(row['min_threshold'])
            brand, _ = Brand.objects.get_or_create(key=row['key'], defaults={'name': row['key']})
            BrandThreshold.objects.create(version=version, min_threshold=threshold, brand=brand)
        except Exception:
            errorJson = dict(id=d['id'], error=traceback.format_exc())
            errors.append(errorJson)
        else:
            successes += 1
    response = {'batch_id': id, 'errors': errors, 'successes': f'{successes}/{dct["pagination"]["totalCount"]}'}
    return JsonResponse(response, safe=False)


@csrf_exempt
def load_item_file(request):
    id = json.loads(request.body)['batch_id']
    dct = FlatFileApi().fetch_rows_by_batch_id(id)
    errors = list()
    successes = 0
    for d in dct['data']:
        try:
            row = d['mapped']
            item_key = row['item_key']
            brand_key = row['brand']
            category_key = row['category']
            banner, region = row['banner'], row['region']
            namespace = row['namespace'] or f'namespace_for_{banner}_{region}'
            brand, _ = Brand.objects.get_or_create(key=brand_key, defaults={'name': brand_key})
            category, _ = CategoryTree.objects.get_or_create(key=category_key, defaults={'name': category_key})
            Item.objects.create(item_key=item_key, namespace=namespace, banner=banner, category=category, brand=brand)
        except Exception:
            errorJson = dict(id=d['id'], error=traceback.format_exc())
            errors.append(errorJson)
        else:
            successes += 1
    response = {'batch_id': id, 'errors': errors, 'successes': f'{successes}/{dct["pagination"]["totalCount"]}'}
    return JsonResponse(response, safe=False)


class EmbedTokenView:
    BRAND_EMBED_PRIVATE_KEY = "WV5ups3cIjAkgmp6PdZsHwDUXuCXXe5N9y9yiGGSvahQewRV1c0VJiTVI8L7H5YZ"
    BRAND_EMBED_ID = "897b2c8b-123e-428c-a51d-354b9b834426"
    ITEM_EMBED_PRIVATE_KEY = "smHENOcmAIUbWq42792RJdmZi95sLzIJnE4izxHncIEwtuLbCwHhG6qcaqtv79cm"
    ITEM_EMBED_ID = "acf91595-476b-4338-9e7e-0621b7c49d01"

    def get_token(self, request):
        sub = request.POST['user_id']
        load_type = request.POST['type']
        if load_type == 'brand':
            embed_id = self.BRAND_EMBED_ID
            priv_key = self.BRAND_EMBED_PRIVATE_KEY
        elif load_type == 'item':
            embed_id = self.ITEM_EMBED_ID
            priv_key = self.ITEM_EMBED_PRIVATE_KEY
        tok = jwt.encode({'embed': embed_id, 'sub': sub}, key=priv_key)
        result = {'type': load_type, 'user_id': sub, 'token': tok}
        return JsonResponse(result)
