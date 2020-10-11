from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    # What fields to display in admin dashboard
    list_display = (
        'name',
        'user_id',
        'email',
        'contact_date',
    )

    search_fields = (
        'name',
        'email',
    )

    list_per_page = 25

    # Orders contacts by date
    ordering = ('contact_date',)


admin.site.register(Contact, ContactAdmin)
