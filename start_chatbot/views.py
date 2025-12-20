from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from rest_framework.response import Response
from . models import Product
from . serializers import ProductSerializer, RegistrationSerializer

from rest_framework.decorators import api_view

from rest_framework import status
from rest_framework.authtoken.models import Token


def chatbot_start(request):
    return HttpResponse("Chatbot Started!")


@api_view(['GET', 'POST'])
def product_list(request, format=None):

    if request.method == 'GET':

        # Get all of the products / Get a list of all the products

        products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)



    if request.method == 'POST':

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, pk, format=None):

    # Use get_object_or_404 instead of try/except DoesNotExist
    product = get_object_or_404(Product, id=pk)


    if request.method == 'GET':

        serializer = ProductSerializer(product)

        return Response(serializer.data)


    elif request.method == 'PUT':

        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def register(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'Successfully registered a new user!'
            ## This is by default in login api, we are returning it during registration as well
            auth_token = Token.objects.get(user=user).key
            data['token'] = auth_token

        else:

            data = serializer.errors
            
                
        return Response(data)    