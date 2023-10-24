from django.contrib import admin
from materials.models import Section, Materials, Tests


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title',)


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'section')
    list_filter = ('title', 'section')


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    list_display = ('materials', 'question', 'correct_answer')
    list_filter = ('materials',)
