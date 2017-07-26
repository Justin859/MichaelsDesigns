from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['about', 'contact', 'product', 'services', 'anniversary']

    def location(self, item):
        return reverse(item)