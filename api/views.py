from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes


# Function based views #

@api_view(['GET'])
def secretJoke1(request):
    print("\n\n Hit on Joke 1 \n\n")
    headers = {}

    return Response(status=200,content_type="application/json",
                    headers=headers,
                    data={'success':1,'error':None,'result':"Joke 1 Here"})

@api_view(['GET'])
def secretJoke2(request):
    print("\n\n Hit on Joke 2 \n\n")
    headers = {}

    return Response(status=200,content_type="application/json",
                    headers=headers,
                    data={'success':1,'error':None,'result':"Joke 2 Here"})


@api_view(['GET'])
def secretJoke3(request):

    print("\n\n Hit on Joke 3 \n\n")

    headers = {}

    return Response(status=200,content_type="application/json",
                    headers=headers,
                    data={'success':1,'error':None,'result':"Joke 3 Here"})
