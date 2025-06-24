from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'contact', 'realizations']  # názvy URL podľa urls.py

    def location(self, item):
        return reverse(item)
