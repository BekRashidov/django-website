from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from django.views.generic import ListView,DetailView,CreateView,View
from .models import Post
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import CommentForm
from django.core.mail import send_mail



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})




def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first-name']
        email = request.POST['email']
        message = request.POST['message']

        # send an e-mail
        send_mail(
            first_name,#subject
            message,#message
            email,#from email
            ['ramazonqahhorov@gmail.com'],#to email


        )

        return render(request, 'contact1.html', {'first_name': first_name})    

    else:
        return render(request, 'contact1.html', {})    





