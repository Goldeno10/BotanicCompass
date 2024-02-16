
from django.contrib import admin
from django import forms
from . import models


class CustomTextareaWidget(forms.Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({'rows': 1, 'cols': 70})
        super().__init__(attrs=attrs)


class HausaNameInline(admin.TabularInline):
    formfield_overrides = {
        models.models.TextField: {'widget': CustomTextareaWidget},
    }
    model = models.HausaName
    min_num = 1
    max_num = 10
    extra = 0


class CommonNameInline(admin.TabularInline):
    formfield_overrides = {
        models.models.TextField: {'widget': CustomTextareaWidget},
    }
    model = models.CommonName
    min_num = 1
    max_num = 10
    extra = 0


class SynonymInline(admin.TabularInline):
    formfield_overrides = {
        models.models.TextField: {'widget': CustomTextareaWidget},
    }
    model = models.Synonym
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(models.PlantData)
class PlantDataAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.models.TextField: {'widget': CustomTextareaWidget},
    }
    list_display = ["scientific_name", "family",
                    "display_hausa_name", "display_common_name", "display_synonym"]
    inlines = [HausaNameInline, CommonNameInline, SynonymInline]
    search_fields = ['common_name', 'family',
                     'hausa_name', 'scientific_name', 'synonym']
    list_per_page = 10

    def display_hausa_name(self, obj):
        return ", ".join([hn.name for hn in obj.hausa_name.all()])
    display_hausa_name.short_description = "Hausa Name"

    def display_common_name(self, obj):
        return ", ".join([cn.name for cn in obj.common_name.all()])
    display_common_name.short_description = "Common Name"

    def display_synonym(self, obj):
        return ", ".join([syn.name for syn in obj.synonym.all()])
    display_synonym.short_description = "Synonym"
