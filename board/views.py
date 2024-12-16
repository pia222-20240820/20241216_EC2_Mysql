from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'board/post_list.html',{'posts':posts})

def post_detail(request):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'board/post_detail.html',{'post':post})

