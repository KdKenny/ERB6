from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'message_updated_date', 'listing', 'user_id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('contact_date', 'message_updated_date')
    list_per_page = 25
    readonly_fields = ('contact_date', 'message_updated_date')

    def get_list_display(self, request):
        return self.list_display

admin.site.register(Contact, ContactAdmin)