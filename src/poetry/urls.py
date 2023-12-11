from django.urls import path
# from django.views.decorators.cache import cache_page
from django.conf.urls.static import serve
from website import settings
from poetry.views import PoetryList, PoetryDetail

urlpatterns = [
    path('poetry/', PoetryList.as_view(), name='poetry'),  # cache_page(60*10)
    path('poetry/<int:pk>', PoetryDetail.as_view(), name='stih_detail'),
]


# if settings.DEBUG:
#     urlpatterns += [path(settings.MEDIA_URL[1:], serve, {"document_root": settings.MEDIA_ROOT})]
