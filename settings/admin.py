from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from settings.models import Setting


class SettingAdmin(SummernoteModelAdmin):
    list_display=['name','call_us','email_us']
    # list_filter=['']
    search_fields=['name','subtitle']
    summernote_fields=['subtitle',]


admin.site.register(Setting,SettingAdmin)

