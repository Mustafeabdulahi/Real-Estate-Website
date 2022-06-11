from django.contrib import admin

# Register your models here.
from .models import Realtor
class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id', 'is_mvb', 'name', 'email', 'hire_date')
	list_display_links = ('id', 'name')
	list_editable = ('is_mvb',)
	search_fields = ('name',)

admin.site.register(Realtor, RealtorAdmin)
