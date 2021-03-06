import os.path
from rollyourown.seo.admin import register_seo_admin
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from condition.seo.seo import SEOMetadata
register_seo_admin(admin.site, SEOMetadata)
admin.autodiscover()

urlpatterns = patterns('',
    #('^$', search),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', 
    { 'document_root': os.path.join(os.path.dirname(__file__), 'images')}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
    { 'document_root': os.path.join(os.path.dirname(__file__), 'uploads')}),
    # Examples:
    #url(r'^$', 'condition.views.index', name='index'),
    url(r'', include('condition.catalog.urls')),
    url(r'', include('condition.thermal.urls')),
    url(r'', include('condition.ventilation.urls')),
    url(r'', include('condition.services.urls')),
    url(r'', include('condition.prepared.urls')),
    url(r'', include('condition.news.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
