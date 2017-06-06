from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^impressum/', views.impressum, name="impressum"),
    url(r'(?P<artikel_id>[0-9]+)/$', views.view_artikel, name="view_artikel"),
]