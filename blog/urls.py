from django.urls import path

from . import views

urlpatterns = [
    path('del_post/del/<int:id_post>/', views.del_postagem, name="del_post"),
    path('post/edit/<int:id_post>/', views.edit_postagem, name="edit_post"),
    path('post/<int:id_post>/', views.postagem, name="ver_post"),
    path('add_post/', views.add_postagem, name="add_post"),
    path('', views.index, name='index'),
    path('post/ocultos/', views.ocultos, name='ocultos'),
    path('add_comentario/<int:id_postagem>/', views.add_comentario, name='add_comentario'),
    path('post/edit/comentario/<int:id_comentario>/', views.edit_comentario, name="edit_comentario"),
    path('post/del/comentario/<int:id_comentario>/', views.del_comentario, name="del_comentario"),
]
