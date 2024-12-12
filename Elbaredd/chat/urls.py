from . import views
from django.urls import path
from django.conf.urls.static import static
urlpatterns = [
       path("", views.login, name="index"),
       path("create", views.create, name="index1"),
       path("loging", views.loging, name="index2"),
       path("creating", views.creating, name="index3"),
       path("chatRoom", views.chatRoom, name="index4"),
       path("chatRoom/newMessage", views.newMessage, name="index5"),
   
]