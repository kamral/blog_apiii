from django.shortcuts import render
from .serializers import PostSerializer
# Create your views here.
from .models import Post
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly


class PostApiView(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


