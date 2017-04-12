from django.contrib import admin

from .models import Question, Choice



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):

    # Adjust which fields get shown on list display.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

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

    # Add choices as an inline field to a question.
    inlines = [ChoiceInline]

    # Add a filter that allows filtering by date.
    list_filter = ['pub_date']

    # Add a search box that allows searching by question text.
    search_fields = ['question_text']

    # Example: Set the order of fields to appear, no fieldsets.
    # fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice);