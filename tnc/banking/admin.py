from django.contrib import admin

from .models import DKBTransaction


class DKBTransactionAdmin(admin.ModelAdmin):
    list_display = ("value_date", "receiver", "amount")


admin.site.register(DKBTransaction, DKBTransactionAdmin)
