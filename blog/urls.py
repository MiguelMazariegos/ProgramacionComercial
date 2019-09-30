from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('pub/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('pub/new', views.post_new, name='nueva_pub'),
    path('post/<int:pk>/edit/', views.post_edit, name='editar_pub'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
