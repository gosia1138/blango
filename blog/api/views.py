from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObjects
from blog.api.serializers import PostSerializer, TagSerializer
from blog.models import Post, Tag
from rest_framework import generics
from rest_framework import generics, viewsets


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObjects]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer