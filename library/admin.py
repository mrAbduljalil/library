from django.contrib import admin
from .models import Authors, Categories, Books, Reviews

@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'availability', 'format', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('availability', 'format', 'categories')
    filter_horizontal = ('categories',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating')
    search_fields = ('book__title', 'user')
    list_filter = ('rating',)
