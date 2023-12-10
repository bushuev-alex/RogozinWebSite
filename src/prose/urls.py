from django.urls import path
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap

from prose.views import (Prose, LivedDetail, ThoughtsDetail, PagesDetail,
                         redirect_to_prose, get_about_info, main_page)

from prose.sitemap import StaticViewSitemap, DynamicViewLived, DynamicViewThoughts, DynamicViewPages

sitemaps = {
   'static': StaticViewSitemap,
   'lived': DynamicViewLived,
   'thoughts': DynamicViewThoughts,
   'pages': DynamicViewPages
}


urlpatterns = [
   path('', main_page, name='main'),  # cache_page(60*10)
   path("about/", get_about_info, name='about'),

   path('prose/', Prose.as_view(), name='prose'),  # cache_page(60*10)
   path('prose/<int:pk>/', redirect_to_prose, name='to_prose'),

   path('prose/lived/<int:pk>/', LivedDetail.as_view(), name='lived'),
   path('prose/lived/<int:pk>/jump_to_page/', LivedDetail.as_view(), name='lived_jump_to_page'),

   path('prose/thoughts/<int:pk>/', ThoughtsDetail.as_view(), name='thoughts'),
   path('prose/thoughts/<int:pk>/jump_to_page/', ThoughtsDetail.as_view(), name='thoughts_jump_to_page'),

   path('prose/pages/<int:pk>/', PagesDetail.as_view(), name='pages'),
   path('prose/pages/<int:pk>/jump_to_page/', PagesDetail.as_view(), name='pages_jump_to_page'),

   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
