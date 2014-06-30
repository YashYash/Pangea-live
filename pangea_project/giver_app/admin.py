from django.contrib import admin
from giver_app.models import Giver


class GiverAdmin(admin.ModelAdmin):
    list_display = ("name", "posted", "video")
    search_fields = ("name",)

admin.site.register(Giver, GiverAdmin)

