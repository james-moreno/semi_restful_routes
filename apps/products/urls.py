from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.products, name="products"),
    url(r'^new$', views.new_product, name="new_product"),
    url(r'^create$', views.create_new_product, name="create_new_product"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name="destroy"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^update/(?P<id>\d+)$', views.update, name="update"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit")
]
