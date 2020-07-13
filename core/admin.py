from django.contrib import admin
from . models import Author, Category, Journal

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_author', 'get_categories', 'publish_date', 'views', 'reviewed']
    list_display_links = ['title', 'views', 'reviewed', 'publish_date']
    search_fields = ['title', 'get_author', 'publish_date']

    def get_author(self, obj):
        return obj.author.name

    get_author.short_description = 'Author'
    get_author.admin_order_field = 'author__name'

    def get_categories(self, obj):
        return "\n".join([p.name for p in obj.categories.all()])

admin.site.register(Author)
admin.site.register(Category)
