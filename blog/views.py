from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def listar_pub(request):
    pubs = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_pub.html', {'pubs': pubs})
