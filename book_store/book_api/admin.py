from django.contrib import admin
from .models import Author, Category, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','created_at')
    search_fields=('name',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin)  :
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'price', 'in_stock')
    list_filter = ('in_stock', 'author', 'categories')
    search_fields = ('title', 'isbn', 'author__name')
    date_hierarchy = 'published_date'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('book__title', 'user__username')  
