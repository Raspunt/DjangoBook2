from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from Polls.TelegaFiles.telegaAlert import SendMessage


from . models import *




class BookAdmin(admin.ModelAdmin):
    fields = ('title','Author','description','slug','image','Rewiew','genreTree','like') 
    list_display = ('title','showImag')
    filter_horizontal = ('Author','comments','genreTree','like')

    prepopulated_fields = {
        "slug":("title",),
    }

    def save_model(self, request, obj, form, change):
        obj.save()
        message = 'появилась новая книга от:\n'

        for author in obj.Author.all():
            message += str(author) + '\n'

        message += "Жанра:\n"
        
        for genre in obj.genreTree.all():
            message += str(genre) + "\n"

        SendMessage(message)

    
    def showImag(self,obj):
        return mark_safe (f'<img src="/media/{obj.image}" width ="80"  height="80">')
    
    showImag.__name__ = "image"

class GenreAdmin(DraggableMPTTAdmin):

    prepopulated_fields = {
        "slug":("title",),
    }


class AuthorAdmin(admin.ModelAdmin):


    prepopulated_fields = {
        "slug":("Name",),
    }



    



admin.site.register(Genre,GenreAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Comments)
admin.site.register(Book,BookAdmin)
admin.site.register(Rewiew)

