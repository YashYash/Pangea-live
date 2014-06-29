from django.contrib import admin
from charity_app.models import Charity


class CharityAdmin(admin.ModelAdmin):
    list_display = ("name", "posted", "video")
    search_fields = ("name",)

admin.site.register(Charity, CharityAdmin)
