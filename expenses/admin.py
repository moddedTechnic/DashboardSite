from django.contrib import admin

from expenses.models import AmortisationTarget, Transaction

admin.site.register(AmortisationTarget)
admin.site.register(Transaction)
