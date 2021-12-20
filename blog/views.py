from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Posts


# Create your views here.
def say_hello(request):
    return HttpResponse('Hello World')


def get_real_posts(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'post_list.html', context)


def post_detail(request, id):
    try:
        post = models.Post.objects.get(id=id)
        try:
            comment = models.Comment.objects.filter(post_id=id).order_by('created_data')
        except models.Comment.DoesNotExist:
            return HttpResponse('No Comments')

    except models.Post.DoesNotExist:
        raise Http404('Post does not exist, baby')

    return render(request, 'post_detail.html', {'post': post, 'post_comment': comment})


def add_comment(request):
    method = request.method
    if method == 'Post':
        form = forms.CommentForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return HttpResponse('Comment Created Successfully')
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment.html', {'form': form})
