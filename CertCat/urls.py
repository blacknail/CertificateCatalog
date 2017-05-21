from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cert_list, name='index'),
    url(r'^certread', views.cert_read, name='cert_read'),
    url(r'^certs', views.cert_list, name='cert_list'),
    url(r'^editorm', views.edit_orm, name='edit_orm'),
    url(r'^editraw', views.edit_raw, name='edit_raw'),
    #url(r'^catalog$', views.catalog, name='catalog'),
]