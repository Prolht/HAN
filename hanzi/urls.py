from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from hanzi import views


urlpatterns = [
    url(r'^characters/', views.CharactersListView.as_view()),
    url(r'^characters/(?P<id>[0-9]+)/$', views.CharactersView.as_view()),
	url(r'^search/', views.CharactersSearchView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)