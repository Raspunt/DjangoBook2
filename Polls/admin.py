from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin


from . models import *




class BookAdmin(admin.ModelAdmin):
    list_display = ('title','showImag')
    filter_horizontal = ('Author','comments','genreTree')

    prepopulated_fields = {
        "slug":("title",),
    }

    def showImag(self,obj):
        return mark_safe (f'<img src="/media/{obj.image}" width ="80"  height="80">')
    
    showImag.__name__ = "image"

class GenreAdmin(DraggableMPTTAdmin):

    prepopulated_fields = {
        "slug":("title",),
    }

    



admin.site.register(Genre,GenreAdmin)
admin.site.register(Author)
admin.site.register(Comments)
admin.site.register(Book,BookAdmin)

