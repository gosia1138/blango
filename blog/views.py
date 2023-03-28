from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm
from django.shortcuts import get_object_or_404
import logging
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils import timezone 

logger = logging.getLogger(__name__)

# @cache_page(60 * 5)
@vary_on_cookie
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Posts: %s", len(posts))
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    logger.warning("Post detail view called")
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )