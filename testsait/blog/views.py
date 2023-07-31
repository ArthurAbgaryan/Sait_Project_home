from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
    
# Create your views here.
