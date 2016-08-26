from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from comment.models import Comment

# Create your views here.
def new(request):
    form = request.POST
    comment_text = form.get('comment')
    user = request.user

    comment = Comment.objects.create(author=user)
    comment.comment = comment_text
    comment.author = user
    comment.save()

    return redirect(reverse('home:index'))
