from django.contrib import admin
from setlist.models import *

class LinkInline(admin.TabularInline):
    model = Link

class ArtistAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    inlines = (LinkInline,)

class LinkAdmin(admin.ModelAdmin):
    pass

class FeatureRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Artist,         ArtistAdmin)
admin.site.register(Song,           SongAdmin)
admin.site.register(Link,           LinkAdmin)
admin.site.register(FeatureRequest, FeatureRequestAdmin)
