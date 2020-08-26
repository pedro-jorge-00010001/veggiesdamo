from django.conf.urls import url
from . import views

app_name = 'mainApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loja/$', views.store, name='store'),
    url(r'^loja/(?P<prod_type>[-\w]+)/$', views.products, name='products'),
    url(r'^loja/(?P<prod_type>[-\w]+)/product/(?P<prod_id>[0-9]+)/$',
        views.product, name='product'),
]
