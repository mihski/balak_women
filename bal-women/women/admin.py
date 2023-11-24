from django.contrib import admin

from .models import Women, Category


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)  #  возможность редактировать


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',"slug")
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Women, WomenAdmin)

# class WomenInline(admin.TabularInline):
#     model = Women
#
#
# @admin.register(Women)
# class WomenAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (
#             "Основная информация",
#             {
#                 "fields": (
#                     "title",
#                     "content",
#
#                     "is_published",
#
#                 )
#             },
#         ),
#     )
#     inlines = (WomenInline,)
