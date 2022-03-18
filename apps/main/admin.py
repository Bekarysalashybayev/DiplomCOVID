from django.contrib import admin

# Register your models here.
from apps.main.models import *


@admin.register(Video)
class BlockAdmin(admin.ModelAdmin):
    list_display = ["name", "link"]
    search_fields = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name"]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name"]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "type", "status", "category"]
    search_fields = ["title"]


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]
    search_fields = ["question"]


@admin.register(Covid)
class CovidAdmin(admin.ModelAdmin):
    list_display = ["city", "get_sick_plus", "recovered_plus",
                    "get_sick_minus", "recovered_minus", "modified"]
    search_fields = ["city"]
