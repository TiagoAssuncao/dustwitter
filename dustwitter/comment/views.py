from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from comment.models import Comment

# Create your views here.
def new(request):
    form = request.POST
    comment_text = form.get('comment')

    comment = Comment.objects.create()
    comment.comment = comment_text
    comment.save()

    return redirect(reverse('home:index'))
