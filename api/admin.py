from django.contrib import admin

from .models import TextClassification


@admin.register(TextClassification)
class TextClassificationAdmin(admin.ModelAdmin):
    model = TextClassification
    # fields = '__all__'
