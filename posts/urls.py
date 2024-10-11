from django.urls import path
from . import views
urlpatterns = [
    path('api/posts/',views.post_list_create,name='post-list-create')
]