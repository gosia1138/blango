from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObjects
from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework import generics


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObjects]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
