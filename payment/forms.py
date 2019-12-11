from django import forms


class CashPaymentForm(forms.Form):
    street = forms.CharField(
        max_length=100,
        help_text='Enter street'
    )
    building_number = forms.CharField(
        max_length=100,
        help_text='Enter house / building number'
    )
    unit_number = forms.CharField(
        max_length=100,
        help_text='Enter house / building number'
    )
    other_instructions = forms.CharField(
        max_length=1000,
        help_text='Enter special instructions'
    )


class PaypalPaymentForm(CashPaymentForm):
    PayPal_username = forms.CharField(
        max_length=100,
        help_text='Enter PayPal Username'
    )
    PayPal_password = forms.CharField(
        max_length=100,
        help_text='Enter PayPal Password'
    )


class CreditCardPaymentForm(CashPaymentForm):
    card_number = forms.CharField(
        max_length=100,
        help_text='Enter credit card number'
    )
    name_on_card = forms.CharField(
        max_length=100,
        help_text='Enter name on card'
    )
    expiration_date = forms.DateField(
        widget=forms.SelectDateWidget
    )
    cvv = forms.CharField(
        label=("CVV"),
        max_length=20,
        help_text='Enter CVV'
    )
