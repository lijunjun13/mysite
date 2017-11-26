from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views


urlpatterns = [
    url(r'^$', learn_views.home, name='home'),
    url(r'^detail/', learn_views.detail, name='detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^graph/', learn_views.graph, name='graph'),
]