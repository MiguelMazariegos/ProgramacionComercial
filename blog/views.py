from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
from django.shortcuts import render, get_object_or_404

# Create your views here.
def listar_pub(request):
    pubs = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})


def detalle_pub (request, pk):
    pub = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle_pub.html', { 'pub': pub })
