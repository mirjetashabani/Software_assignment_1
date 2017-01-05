from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import *
from .models import *
from .forms import BlogForm
from django.contrib.auth.decorators import permission_required


def show_blog(request, item_id):
    try:
        entry = Blog.objects.get(id=item_id, owner=request.user.id)
        return render(request, "one_blog.html", {"entry": entry})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")


def show_all_blogs(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "blog.html", {"entries": Blog.objects.filter(owner=request.user.id),
                                         "tags": Tag.objects.all(),
                                         "form": form})


def index(request):
    return HttpResponse('<a href="entries> Blog Page</a>')

@permission_required('is_superuser')
def show_all_entries(request):
    return render(request, "blog.html", {"entries": Blog.objects.all()})

@permission_required('is_superuser')
def show_specific_for_user(request, user_id):
    return render(request, "blog.html", {"entries": Blog.objects.filter(owner=user_id)})
