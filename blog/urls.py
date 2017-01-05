from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^entries/all/user/(?P<user_id>[0-9]+)$',show_specific_for_user),
    url(r'^entries/(?P<item_id>[0-9]+)', show_blog),
    url(r'^entries/$', show_all_blogs),
    url(r'^entries/all',show_all_entries),
    url(r'^$', index),
]



