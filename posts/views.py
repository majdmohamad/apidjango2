from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Posts
from .serializers import PostSerializers

# Create your views here.
@api_view(['GET','POST'])
def post_list_create(request):
    if request.method=='GET':
        posts=Posts.objects.all()
        serializer=PostSerializers(posts,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
