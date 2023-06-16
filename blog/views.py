from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Post, Comments
from django.views.generic.edit import CreateView
from .forms import CommentsForm


def PostList(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def PostDetail(request, pk):
    post_detail = Post.objects.get(pk=pk)
    context = {'post_detail': post_detail}
    return render(request, 'blog/detail.html', context)


def Commnet(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(reverse('detail', kwargs={'pk': pk}))
    else:
        comment_form = CommentsForm()
    context = {'comment_form': comment_form}
    return render(request, 'blog/commentForm.html', context)


