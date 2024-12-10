from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views import View

# def home(request) :
#     return render()


def main(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {"blogs":blogs})

def contact(request):
    return render(request, 'detail.html')

def detail(request, pk):
    article = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', {"article": article})

class Detail(View):
    def get(request, pk):
        article = get_object_or_404(Blog, pk=pk)
        return render(request, 'detail.html', {"article": article})
    
    def post(request, form=None):
        pass