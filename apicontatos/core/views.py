from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import hubspot
from pprint import pprint
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
from hubspot.crm.properties import PropertyCreate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
import json
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


@api_view(['POST'])
def get_access_token(request):
    if request.method == 'POST':
        print(request.data)
        if 'refresh_token' in request.data:
            print('to aqui')
            client = hubspot.Client.create(access_token=request.data['access_token'])

            try:
                api_response = client.auth.oauth.refresh_tokens_api.get_refresh_token(token=request.data['token'])
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling refresh_tokens_api->get_refresh_token: %s\n" % e)
        elif 'code' in request.data:
            print('to aqui')
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
            payload = {
                "grant_type": 'authorization_code',
                "client_id": "1f354f0f-7797-423e-b7c7-be178f48d51f",
                "client_secret": "7a4af898-e152-4b4d-a785-b1b82c90a8fe",
                "redirect_uri": "http://localhost:3000/",
                "code": request.data['code']
            }

            # print(json_object)
            # if ('message' and 'status') in json_object:
            #     payload['grant_type'] = request.data['refresh_token']
            #     del payload['code']
            #     request_token = requests.post('https://api.hubapi.com/oauth/v1/token',
            #                                   headers=headers, data=payload)
            # request_token = requests.post('https://api.hubapi.com/oauth/v1/token',
            #                               headers=headers, data=payload)
            # access_token = requests.get('https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false',
            #                             headers={'Content-Type': 'application/json', "Authorization": "Bearer " + json_object['access_token']})
            request_token = requests.post('https://api.hubapi.com/oauth/v1/token',
                                        headers=headers, data=payload)
            json_object = json.loads(request_token.content.decode('utf-8'))
            print(json_object)
            return JsonResponse({"access_token": json_object['access_token'], 'refresh_token': json_object['refresh_token']}, safe=False)
        return JsonResponse({}, safe=False)

# def contatos_list(request):
#     if request.method == "GET":


@api_view(['POST'])
def contatos(request):
    if request.method == "POST":
        access_token = requests.get('https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false',
                                    headers={'Content-Type': 'application/json', "Authorization": "Bearer " + request.data['access_token']})
        print("to aqui", access_token.content)
    return JsonResponse({'123': '1231'}, safe=False)


@api_view(['POST'])
def create_contato(request):
    if request.method == "POST":
        client = hubspot.Client.create(
            access_token=request.data['access_token'])
        # try:
        x = requests.get('https://api.hubapi.com/crm/v3/properties/contacts/teste?archived=false',
                         headers={"Authorization": "Bearer " + request.data['access_token']})

        json_object = json.loads(x.content.decode('utf-8'))
        print(json_object)
        if ('status' and 'message') in json_object:
            print('to aqui')
            property_create = PropertyCreate(name="teste", label="Peso", type="string", field_type="text", group_name="contactinformation", options=[
            ], display_order=2, has_unique_value=False, hidden=False, form_field=True)
            propriedade = client.crm.properties.core_api.create(
                object_type='contacts', property_create=property_create)
        # x = requests.get('https://api.hubapi.com/crm/v3/properties/contacts/wilds?archived=false',
        #                  headers={"Authorization": "Bearer " + request.data['access_token']})
        # print(x.content)
        # api_response = client.crm.properties.core_api.get_by_name(object_type="contacts", property_name="wids", archived=False)
        # print("to aqui ", api_response)
        # pprint("toaqui ",api_response)
        # except ApiException as e:
        # print("Exception when calling core_api->get_by_name: %s\n" % e)
        # if not api_response:
        #     property_create = PropertyCreate(name="weight", label="Peso", type="string", field_type="text", group_name="contactinformation", options=[
        #     ], display_order=2, has_unique_value=False, hidden=False, form_field=True)
        #     propriedade = client.crm.properties.core_api.create(
        #         object_type='contacts', property_create=property_create)

        simple_public_object_input = SimplePublicObjectInput(
            properties=request.data['data']['properties'])
        try:
            api_response = client.crm.contacts.basic_api.create(
                simple_public_object_input=simple_public_object_input)
        except ApiException as e:
            print("Exception when calling basic_api->create: %s\n" % e.body)
            x = json.loads(e.body)
            numbers = [int(word)
                       for word in x['message'].split() if word.isdigit()]
            string = ''
            for i in numbers:
                string += str(i)
            pprint(int(string))
            # for i in e.body:
            #     print(i)
            if 'email' in request.data['data']['properties']:
                del request.data['data']['properties']['email']
                SimplePublicObjectInput(
                    properties=request.data['data']['properties'])
                api_response = client.crm.contacts.basic_api.update(
                    contact_id=int(string), simple_public_object_input=simple_public_object_input)
                # pprint(api_response)
            # print("Exception when calling basic_api->create: %s\n" % e)
        # access_token = requests.get('https://api.hubapi.com/crm/v3/objects/contacts',
        #                             headers={'Content-Type': 'application/json', "Authorization": "Bearer " + request.data['access_token']}, data=request.data['data'])
        # print("to aqui", access_token.content)
    return JsonResponse({'123': '1231'}, safe=False)


def auth(request):
    return redirect('https://app.hubspot.com/oauth/authorize?client_id=1f354f0f-7797-423e-b7c7-be178f48d51f&redirect_uri=http://localhost:8000/&scope=crm.objects.contacts.read%20crm.objects.contacts.write%20crm.schemas.contacts.read%20crm.schemas.contacts.write')
