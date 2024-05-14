from django.urls import path
from .views import index, post_detail, post_table

urlpatterns=[
  path("", index),
  path("post/<slug>", post_detail, name="blog-post-detail"),
  path("post-table/", post_table, name="blog-post-table"),
]