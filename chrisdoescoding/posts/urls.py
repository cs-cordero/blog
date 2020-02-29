from django.urls import path

from posts import feed, views

urlpatterns = [
    path("latest/", views.LatestPostView.as_view(), name="latest"),
    path("<int:pk>/", views.PostView.as_view(), name="post"),
    path("rss/", feed.RssPostFeed(), name="rss"),  # type: ignore
    path("atom/", feed.AtomPostFeed(), name="atom"),  # type: ignore
    path("random/", views.RandomPostView.as_view(), name="random"),
    path("", views.AllPostsView.as_view(), name="list"),
]
