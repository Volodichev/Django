from django.urls import path
from . import views

urlpatterns = [
    path('tag/<slug:slug>/', views.PostListView.as_view(), name='tag'),
    path("<slug:category_slug>/", views.PostListView.as_view(), name="category"),
    path("<slug:category>/<slug:slug>/", views.PostView.as_view(), name="detail_post"),

    # path("", views.PostListView.as_view()),
]


