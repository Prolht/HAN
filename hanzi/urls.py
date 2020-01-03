from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from hanzi import views


urlpatterns = [
    url(r'^list/$', views.CharactersListView.as_view()),  # 列表
    url(r'^character/', views.CharacterView.as_view()),
	url(r'^search/', views.CharactersSearchView.as_view()),
	url(r'^upload/', views.uploadImg),
	url(r'^show/', views.showImg),
	url(r'^update/', views.UpdateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
