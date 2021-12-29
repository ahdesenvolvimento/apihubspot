from django.http.response import JsonResponse
from django.shortcuts import redirect, render
import hubspot
from pprint import pprint
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException
from hubspot.crm.properties import PropertyCreate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests


# Create your views here.
def index(request):
    return JsonResponse({"access_token": 'index'}, safe=True)


@api_view(['POST'])
def get_access_token(request, code=None):
    if request.method == 'POST':
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        if code == 1:
            if 'refresh_token' in request.data:
                payload = {
                    "grant_type": 'refresh_token',
                    "client_id": "1f354f0f-7797-423e-b7c7-be178f48d51f",
                    "client_secret": "7a4af898-e152-4b4d-a785-b1b82c90a8fe",
                    "refresh_token": request.data['refresh_token']
                }
                request_token = requests.post('https://api.hubapi.com/oauth/v1/token',
                                              headers=headers, data=payload)
                json_object = json.loads(request_token.content.decode('utf-8'))
                return JsonResponse({"access_token": json_object['access_token'], 'refresh_token': json_object['refresh_token']}, safe=False)
        elif code == 2:
            payload = {
                "grant_type": 'authorization_code',
                "client_id": "1f354f0f-7797-423e-b7c7-be178f48d51f",
                "client_secret": "7a4af898-e152-4b4d-a785-b1b82c90a8fe",
                "redirect_uri": "http://localhost:3000/",
                "code": request.data['code']
            }
            request_token = requests.post('https://api.hubapi.com/oauth/v1/token',
                                          headers=headers, data=payload)
            json_object = json.loads(request_token.content.decode('utf-8'))
            return JsonResponse({"access_token": json_object['access_token'], 'refresh_token': json_object['refresh_token']}, safe=False)


@api_view(['POST'])
def contatos(request):
    if request.method == "POST":
        contatos = requests.get('https://api.hubapi.com/crm/v3/objects/contacts?limit=100&properties=weight&properties=phone&properties=date_of_birth&properties=email&archived=false',
                                headers={'Content-Type': 'application/json', "Authorization": "Bearer " + request.data['access_token']})
        json_object = json.loads(contatos.content.decode('utf-8'))
        return JsonResponse({"contatos": json_object['results']}, safe=False)
    return JsonResponse({'123': '1231'}, safe=False)


@api_view(['POST'])
def create_contato(request):
    if request.method == "POST":
        if request.data['access_token'] is None:
            return JsonResponse({"message":"Você precisa fazer a autenticação no sistema!"})
        client = hubspot.Client.create(
            access_token=request.data['access_token'])
        # Busca pela propriedade peso
        x = requests.get('https://api.hubapi.com/crm/v3/properties/contacts/weight?archived=false',
                         headers={"Authorization": "Bearer " + request.data['access_token']})

        json_object = json.loads(x.content.decode('utf-8'))

        # Se não retornar um dict com essas chaves, é por que a propriedade não existe para essa conta
        if ('status' and 'message') in json_object:
            # Cria a propriedade para a conta
            property_create = PropertyCreate(name="weight", label="Peso", type="string", field_type="text", group_name="contactinformation", options=[
            ], display_order=2, has_unique_value=False, hidden=False, form_field=True)
            propriedade = client.crm.properties.core_api.create(
                object_type='contacts', property_create=property_create)

        simple_public_object_input = SimplePublicObjectInput(
            properties=request.data['data']['properties'])
        try:
            api_response = client.crm.contacts.basic_api.create(
                simple_public_object_input=simple_public_object_input)
            return JsonResponse({"message": "Usuário %s foi criado!" % request.data['data']['properties']['email']}, safe=False)
        except ApiException as e:
            x = json.loads(e.body)

            # Trecho de código para pegar o ID do usuário
            numbers = [int(word)
                       for word in x['message'].split() if word.isdigit()]
            string = ''
            for i in numbers:
                string += str(i)
            # Editar o contato
            if 'email' in request.data['data']['properties']:
                # Deleto a propriedade email
                email = request.data['data']['properties']['email']
                del request.data['data']['properties']['email']
                SimplePublicObjectInput(
                    properties=request.data['data']['properties'])
                api_response = client.crm.contacts.basic_api.update(
                    contact_id=int(string), simple_public_object_input=simple_public_object_input)
                return JsonResponse({"message": "Usuário %s foi editado!" % email}, safe=False)
    return JsonResponse({'message': 'Você precisa preencher os formulários!'}, safe=False)


@api_view(['DELETE'])
def delete_contato(request, pk):
    if request.method == "DELETE":
        client = hubspot.Client.create(
            access_token=request.data['access_token'])
        try:
            api_response = client.crm.contacts.basic_api.archive(contact_id=pk)
            contatos = requests.get('https://api.hubapi.com/crm/v3/objects/contacts?limit=100&properties=weight&properties=phone&properties=date_of_birth&properties=email&archived=false',
                                    headers={'Content-Type': 'application/json', "Authorization": "Bearer " + request.data['access_token']})
            json_object = json.loads(contatos.content.decode('utf-8'))
            return JsonResponse({"contatos": json_object['results']}, safe=False)
        except ApiException as e:
            print("Exception when calling basic_api->archive: %s\n" % e)
