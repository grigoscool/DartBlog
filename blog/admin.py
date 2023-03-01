from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tag, Category, Post


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('create_at', 'is_published', 'tag')
    list_display = (
        'id', 'title', 'author', 'create_at', 'views', 'get_photo',
        'category', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'category')
    save_on_top = True
    fields = (
        'id', 'title', 'author', 'create_at', 'views',
        'is_published', 'slug', 'content',
        'photo', 'get_photo', 'category', 'tag')
    readonly_fields = ('id', 'get_photo', 'create_at')
    search_fields = ('id', 'title', 'author', 'category', 'tag')

    def get_photo(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" width="75" >')

    get_photo.short_description = 'Photo'


admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
