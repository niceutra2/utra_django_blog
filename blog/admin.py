from django.contrib import admin
from blog.models import Post
from ckeditor.widgets import CKEditorWidget

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')


admin.site.register(Post,  PostAdmin)
