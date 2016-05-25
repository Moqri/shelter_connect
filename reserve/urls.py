from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.find_shelter, name='find_shelter'),
	url(r'^reserve$', views.reserve, name='reserve'),
]
