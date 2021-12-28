from django.http.response import JsonResponse
from django.shortcuts import render
from hubspot import HubSpot
from hubspot.auth.oauth import ApiException
import requests


# Create your views here.
def index(request):
    # acesso = 'https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:8000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write'

    # code = request.GET.get('code')
    # r = requests.get(acesso)
    # print(r)
    # x = requests.post('https://api.hubapi.com/oauth/v1/token?grant_type=authorization_code&client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&client_secret=7a4af898-e152-4b4d-a785-b1b82c90a8fe&redirect_uri=http://localhost:8000/&code=%s'%code)
    # print(x)
    
    api_client = HubSpot()
    # # or with api_key
    
    # print(code)
    # api_client = HubSpot(api_key='15669a86-ad37-4192-95cd-dbb950bae4d3')
    # for attr, value in api_client.__dict__.items():
    #     print(attr, value)
    # print(api_client)
    # or with access_token
    # api_client = HubSpot()
    # api_client.access_token = '15669a86-ad37-4192-95cd-dbb950bae4d3'
    try:
        tokens = api_client.auth.oauth.default_api.create_token(
            grant_type="authorization_code",
            redirect_uri='http://localhost:8000/',
            client_id='1f354f0f-7797-423e-b7c7-be178f48d51f',
            client_secret='7a4af898-e152-4b4d-a785-b1b82c90a8fe',
            code='3a3350f-46ea-4c5a-a9b6-63810937562d'
        )
        print(tokens)
    except ApiException as e:
        print("Exception when calling create_token method: %s\n" % e)
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
