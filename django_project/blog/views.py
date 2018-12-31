from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'Date_posted': 'August 27,2018'
    },
    {
        'author': 'CoreasdfS',
        'title': 'Blog Post 2',
        'content': '2nd post content',
        'Date_posted': 'August 227,2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
