from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']  # поля в списке
    list_filter = ['status', 'created', 'publish', 'author']  # возможные фильтры
    search_fields = ['title', 'body']  # строка поиска
    prepopulated_fields = {'slug': ('title',)}  # предзаполнение поля
    raw_id_fields = ['author']  # поисковый виджет вместо выпад. списка
    date_hierarchy = 'publish'  # создание "календаря"
    ordering = ['status', 'publish']  # сортировка по этим полям
