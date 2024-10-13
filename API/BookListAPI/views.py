from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

@api_view(['POST'])
def books(request):
    return Response('list of books', status=status.HTTP_200_OK)

class BookList(APIView):
    def get(self, request):
        author = request.GET.get('author')
        if(author):
            return Response({"message":"list of books by" + author}, status=status.HTTP_200_OK)
        return Response({"message":"list of books"}, status=status.HTTP_200_OK)

# request.GET is the dictionary of the GET variables in the http request made to your server, for example:
#        www.google.com?thisIsAGetVarKey=3&thisIsAnotherOne=hello
# request.GET would be: {"thisIsAGetVarKey": 3, "thisIsAnotherOne":"hello"}
# Because request.GET is a dictionary, it has the method .get() which retrieves a value for a key in the dictionary

    def post(self,request):
        return Response({"message":"new book created"}, status=status.HTTP_201_CREATED)
