from django import forms

PAYMENT_CHOICES = (
    ('P', 'Paystack'),
    ('S', 'Stripe')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = forms.CharField(required=False)

    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = forms.CharField(required=False)
    billing_zip = forms.CharField(required=False)
    same_billing_address = forms.BooleanField(required=False)
    # save_info=forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


# request refund form
class RefundForm(forms.Form):
    ref_code = forms.CharField(widget=forms.TextInput(attrs={

        'placeholder': 'Order reference code'
        # rows:3

    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={

        'placeholder': 'Your Email-address'
        # rows:3

    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
        'placeholder': 'Write your complain'
        # rows:3

    }))