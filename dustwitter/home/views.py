from django.shortcuts import render
from comment.models import Comment

# Create your views here.
def index(request):
    comments = reversed(Comment.objects.all())

    context = {
        "comments": comments
    }

    return render(request, 'home/index.html', context)
