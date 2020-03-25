from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post

posts=[
    {
        'Aurthor':'Ankit Maurya',
        'Title':'All about django',
        'Content':'First Post',
        'Date':'Mar 24,2020'
    },
    {
        'Aurthor':'Amit Maurya',
        'Title':'Not Decided yet',
        'Content':'Second Post',
        'Date':'Jan 26,2020'
    }
]

# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
