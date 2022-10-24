from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from .models import Post, Comments
from django.views.generic.edit import CreateView
from .forms import CommentsForm


#
# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/detail.html'

def PostList(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def PostDetail(request, pk):
    form = CommentsForm()
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            # return redirect('detail')

    post_detail = Post.objects.get(id=pk)
    return render(request, 'blog/detail.html', context={'post_detail': post_detail,
                                                        'form': form})


# def comments(request):
#     form = CommentsForm()
#     if request.method == 'POST':
#         form = CommentsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     return render(request, 'blog/comments.html', {'form': form})
