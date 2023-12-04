from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name="logout"),
     path('edit/', views.edit_user, name="edit_user"),

]
