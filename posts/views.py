# from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    # So the context object is not 'object_list'
    context_object_name = "all_posts_list"