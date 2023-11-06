from django.contrib import admin
from .models import Question, Choice


# Register your models here
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    save_on_top = False
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    #Adding a filter sidebar
    list_filter = ["pub_date"]
    #adding Searching capabilities
    search_fields = ["question_text"]
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)