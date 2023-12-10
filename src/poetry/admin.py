from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from poetry.models import ChildPoetry


class blogadmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'text')
    list_filter = ("title", )
    search_fields = ['title', 'text']
    # prepopulating slug from title
    # prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('text', )


# Register your models here.
admin.site.register(ChildPoetry, blogadmin)
