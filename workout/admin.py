from django.contrib import admin
from .models import Writer

# Register your models here.
'''
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
	inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
	list_display =('choice_text','votes')
	list_filter = ['choice_text']
	search_fields = ['votes']
admin.site.register(Pool, PollAdmin)
admin.site.register(User)
admin.site.register(Choice, ChoiceAdmin)
'''
admin.site.register(Writer)
