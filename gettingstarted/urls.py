from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

from django.contrib import admin
admin.autodiscover()

import designs.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    url(r'^$', designs.views.index, name='index'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/', designs.views.about, name='about'),
    url(r'^contact/', designs.views.contact, name='contact'),
    url(r'^product/', designs.views.product, name='product'),
    url(r'^services/', designs.views.services, name='services'),
    url(r'^anniversary-gift-list', designs.views.anniversary, name="anniversary"),
    url(r'^signup-to-newsletter', designs.views.newsletter_signup, name="newsletter-signup"),
    url(r'^premier-brand/(?P<premier_brand_name>[\w\-\s]+)/$', designs.views.detail, name='detail'),
]
