from blog.api_views import post_detail, post_list
from django.urls import path

urlpatterns = [
    path("posts/", post_list, name="api_post_list"),
    path("posts/<int:pk>/", post_detail, name="api_post_detail"),
]
