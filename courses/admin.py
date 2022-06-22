from django.contrib import admin

from .models import Course, Category, Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id","name","available")
    list_filter = ("available","name")
    search_fields = ('name', "description")
    ordering = ('-name',)
    fieldsets = (
        (None, {
            "fields": (("name",), "available"),
    }),
    ("Advenced options", {
        "fields": ("description", "image"),
        "classes": ("collapse",),
        "description": "Advanced options",
    }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}