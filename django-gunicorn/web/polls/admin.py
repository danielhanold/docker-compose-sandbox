from django.contrib import admin

from .models import Question, Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):

    # Example: Create a fieldset and put specific fields
    # into a fieldset.
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date information', {
            'fields': ['pub_date']
        })
    ]
    inlines = [ChoiceInline]

    # Example: Set the order of fields to appear, no fieldsets.
    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice);