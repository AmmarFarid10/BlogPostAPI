from django.urls import path
from . import views

urlpatterns =[
    #path('searchblog/', views.BlogPostList.as_view(), name='search-blog'),
    path('blogposts/<int:pk>/', views.BlogPostDetail.as_view(), name='blogpost-detail'),

    #path("blogpost/",views.BlogPostListCreate.as_view(),name="blogpost_view_create"),
    #path("blogpost/<int:pk>/",views.BlogPostRetrieveUpdateDestroy.as_view(),name="update")
]