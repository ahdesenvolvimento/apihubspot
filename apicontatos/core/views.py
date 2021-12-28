from django.http.response import JsonResponse
from django.shortcuts import redirect, render
# from hubspot import HubSpot
# from hubspot.auth.oauth import ApiException
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
import requests


# Create your views here.
def index(request):
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}

    if request.GET.get('code') is None:
        # return JsonResponse({"e":"1"}, safe=False)
        return redirect('auth')
        return redirect('https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:8000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write')
    # r = requests.get('https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:8000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write', allow_redirects=True)
    # print(r.content)
    payload = {
        "grant_type": 'authorization_code',
        "client_id": "1f354f0f-7797-423e-b7c7-be178f48d51f",
        "client_secret": "7a4af898-e152-4b4d-a785-b1b82c90a8fe",
        "redirect_uri": "http://localhost:8000/",
        "code": request.GET.get('code')
    }
    print(request.GET.get('code'))
    x = requests.post('https://api.hubapi.com/oauth/v1/token',
                      headers=headers, data=payload)
    import json
    # a= b"{'one': 1, 'two': 2}"
    y = json.loads(x.content.decode('utf-8'))
    # print(y['access_token'] + y['access_token'])
    k = requests.get('https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false',
                     headers={'Content-Type': 'application/json', "Authorization": "Bearer " + y['access_token']})
    print(k.content)
    return JsonResponse({"access_token": y['access_token']}, safe=True)
    # access_token = x.content.access_token
    # x = requests.post('https://api.hubapi.com/oauth/v1/token?grant_type=authorization_code&client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&client_secret=7a4af898-e152-4b4d-a785-b1b82c90a8fe&redirect_uri=http://localhost:8000/&code=%s'%code)
    # print(x)
    # from hubspot.crm.contacts import SimplePublicObjectInput
    # from hubspot.crm.contacts.exceptions import ApiException

    # try:
    #     simple_public_object_input = SimplePublicObjectInput(
    #         properties={"email": "emailtest123124e@example.com", "firstname": "jose",
    #                     "phone": "123456789", "birthday": "2021-01-19"}
    #     )
    #     api_response = api_client.crm.contacts.basic_api.create(
    #         simple_public_object_input=simple_public_object_input
    #     )
    # except ApiException as e:
    #     print("Exception when creating contact: %s\n" % e)
    return JsonResponse({'text': 'text'}, safe=False)


@api_view(['POST'])
def contatos(request):
    print(request.method)
    print(request.data)

def auth(request):
    return redirect('https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:8000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write')