from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from prose.models import ProjitoeNeUgasaet, ThoughtAboutLived, PagesOfHistory


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        return ['about', 'prose']

    def location(self, item):
        return reverse(item)


class DynamicViewLived(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return ProjitoeNeUgasaet.objects.all()


class DynamicViewThoughts(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return ThoughtAboutLived.objects.all()


class DynamicViewPages(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return PagesOfHistory.objects.all()
