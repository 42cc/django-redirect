from django.contrib import admin
from models import Redirect


class RedirectAdmin(admin.ModelAdmin):
    list_display = ['from_url', 'to_url', 'site', 'status']


    def save_model(self, request, object, form, change):
        instance = form.save()
        # for sites that are not in debug mode reload
        # the dynamic urls, i'm not sure if this is the
        # best way though
        return instance

admin.site.register(Redirect, RedirectAdmin)
