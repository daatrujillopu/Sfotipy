from django.contrib import admin

from .models import Track
# Register your models here.


from actions import export_as_excel
class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'track_file', 'album', 'player', 'es_dream_theather')
    list_filter = ('artist', 'album')
    search_fields = ('title', 'artist__first_name', 'artist__last_name')
    list_editable = ('title', 'album')
    actions = (export_as_excel,)
    def es_dream_theather(self, obj):
        return obj.id == 1

    es_dream_theather.boolean = True

admin.site.register(Track, TrackAdmin)