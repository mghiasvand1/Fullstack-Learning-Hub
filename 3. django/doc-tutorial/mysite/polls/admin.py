from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Choice)
# In that form, the “Question” field is a select box containing every question in the database. Django knows that a ForeignKey should be represented in the admin as a <select> box .
# Also note the “Add Another” link next to “Question.” Every object with a ForeignKey relationship to another gets this for free. When you click “Add Another”, you’ll get a popup window with the “Add question” form .
# An inefficient way of adding Choice objects to the system. It’d be better if you could add a bunch of Choices directly when you create the Question object .

class ChoiceInline(admin.TabularInline):    
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # The ModelAdmin class is the representation of a model in the admin interface .
    # fields = ['pubDate', 'questionText']
    # For changing the order of pubDate and questionText in the admin page .
    fieldsets = [
        (None, {'fields' : ['questionText']}),
        ('Date information', {'fields' : ['pubDate'], 'classes' : ['collapse']}),
    ]
    # The first element of each tuple in fieldsets is the title of the fieldset .
    # A list or tuple containing extra CSS classes to apply to the fieldset .
    inlines = [ChoiceInline]
    # When two Django models share a foreign key relation, inlines can be used to expose the related model on the parent model page. This can be extremely useful for many applications .
    # This tells Django: “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices .
    list_display = ('questionText', 'pubDate', 'wasPublishedRecently')
    list_filter = ['pubDate']
    # The type of filter displayed depends on the type of field you’re filtering on .
    search_fields = ['questionText']
    # That adds a search box at the top of the change list. When somebody enters search terms, Django will search the question_text field .

admin.site.register(Question, QuestionAdmin)