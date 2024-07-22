from django.urls import path
from . import views

urlpatterns =  [
    path('',views.index),
    path('get-all-post/',views.GetAllPost),
    path('create-new-post/',views.CreatePost),
    path('deletepost/',views.DeletePost),
    path('update-post/',views.UpdatePost),
]