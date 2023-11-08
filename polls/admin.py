from django.contrib import admin
from .models import Question, Choice


# Register your models here
class ChoiceInline(admin.TabularInline):
    model = Choice
    #This increase the default choice appearing per question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #when True the save button appear on top
    save_on_top = False
    #Fieldset declaration.
    fieldsets = [
        ("Question Information", {"fields": ["question_text"]}),
        ("date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    #Adding a filter sidebar
    list_filter = ["pub_date"]
    #adding Searching capabilities
    search_fields = ["question_text"]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)