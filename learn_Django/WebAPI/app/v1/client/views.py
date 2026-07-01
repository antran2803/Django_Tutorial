from rest_framework import status 
from rest_framework.decorators import api_view ,APIView
from rest_framework.response import Response
from app.models import Client,Post
from .serializers import ClientV1Serializer,PostV1Serializer

# @api_view(['GET','POST'])
# def client_list(request):
#     if request.method == "GET":
#         client = Client.objects.all()
#         serializer = ClientV1Serializer(client, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "POST":
#         serializer =ClientV1Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClientListView(APIView): 
    def get(self,request):
        client  = client.objects.all()
        serializer = ClientV1Serializer(client, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ClientV1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def client_detail(request,pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ClientV1Serializer(client)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ClientV1Serializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def post_list(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostV1Serializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer =PostV1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk): 
    try:
        post =Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer= PostV1Serializer(post)
        return Response(serializer.data,status= status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = PostV1Serializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


