from django.urls import path, include
from rest_framework.authtoken import views
from blog.api.views import PostDetail, PostList
from rest_framework.routers import DefaultRouter
from blog.api.views import TagViewSet

router = DefaultRouter()
router.register("tags", TagViewSet)

urlpatterns = [
    path("posts/", PostList.as_view(), name="api_post_list"),
    path("posts/<int:pk>/", PostDetail.as_view(), name="api_post_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]
