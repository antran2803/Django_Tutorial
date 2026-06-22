from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# admin.site.register(Question)
# replace the above code wtih the class QuestionAdmin
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields' : ['question_text']}),
#         ('Date information', { 'fields': ['pub_date']})
#     ]

# admin.site.register(Question , QuestionAdmin)

# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None , {'fields' : ['question']}),
#         ('Choice information' , {'fields': ['choice_text']}),
#         ('Vote information' , {'fields' : ['votes']})
#     ]

# admin.site.register(Choice ,ChoiceAdmin)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {"fields" : ['question_text']}),
        ('Date information', { 'fields' : ['pub_date'],'classes' : ['collapse']})
    ]
    list_display = ('question_text' , 'pub_date' , 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    inlines = [ChoiceInline]
admin.site.register(Question ,QuestionAdmin)
admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls Admin Portal"
admin.site.index_title = "Welcome to Polls Admin"