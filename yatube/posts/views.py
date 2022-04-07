from django.shortcuts import render

def index(request):
    template = '../templates/posts/index.html'
    return render(request, template)

def group_posts(request, pk):
    template = '../templates/posts/group_list.html'
    return render(request, template)
