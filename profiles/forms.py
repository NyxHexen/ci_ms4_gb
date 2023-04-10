from django import forms
from .models import UserProfile


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "default_phone_number",
            "default_street_address1",
            "default_street_address2",
            "default_town_or_city",
            "default_postcode",
            "default_county",
            "default_country",
        )

    def __init__(self, *args, **kwargs):
        """
        Update label values and set autofocus on phone number.
        """
        super().__init__(*args, **kwargs)
        labels = {
            "default_phone_number": "Phone Number",
            "default_country": "Country",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            self.fields[field].label = labels[field]