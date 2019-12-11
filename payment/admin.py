from django.contrib import admin

from .models import PayPalTransaction, CreditCardTransaction


class PayPalTransactionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['caterer']}),
		(None, {'fields': ['holder']}),
		(None, {'fields': ['paypal_username']}),
		(None, {'fields': ['date_transacted']}),
	]


class CreditCardTransaction(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['card_number']})
	]