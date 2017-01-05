from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', show_todo),
    url(r'^(?P<todo_id>[0-9]+)', get_todo),
]
