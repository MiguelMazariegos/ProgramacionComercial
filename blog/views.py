from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404
from .forms import PublicacionForm
from django.shortcuts import redirect

# Create your views here.
def listar_pub(request):
    pubs = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})


def detalle_pub (request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', { 'pub': pub })


def post_new(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = PublicacionForm()
    return render(request, 'blog/pub_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('detalle_pub', pk=post.pk)
    else:
        form = PublicacionForm(instance=post)
    return render(request, 'blog/pub_edit.html', {'form': form})
