from django.contrib import admin
from .models import Category, Tag, Post, Comment

# from pages.admin import ActionPublish

class ActionPublish(admin.ModelAdmin):
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)



class CategoryAdmin(ActionPublish):
    """Категории блога"""
    list_display = ("id", "name", "parent", "slug", "paginated", "sort", "published")
    list_display_links = ("id", "name", "slug", )
    list_filter = ("parent", )
    # exclude = ("sort", )
    # fieldsets
    # inlines =
    actions = ['unpublish', 'publish']


class CommentsInline(admin.StackedInline): # TabularInline
    model = Comment
    extra = 1


class PostAdmin(ActionPublish):
    """Посты блога"""
    inlines = [CommentsInline]
    filter_horizontal = ("tags",)
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug'),
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'image'),
        }),
        ('Даты', {
            'fields': ('edit_date', 'published_date'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category'),
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('template', 'published', 'status', 'sort', 'viewed'),
        }),
    )

admin.site.register(Category, CategoryAdmin)
# admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
admin.site.register(Comment)


admin.site.site_title = "Еще одни сайт на django"
admin.site.site_header = "Еще одни сайт на django"
