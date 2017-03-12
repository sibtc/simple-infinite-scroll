from django.conf.urls import url

from mysite.blog import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^blog/$', views.ArticlesView.as_view(), name='blog'),
    url(r'^blog/fake/$', views.generate_fake_data, name='generate_fake_data'),
]
