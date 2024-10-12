# from django import forms

# from .models import RSSFeed
# from nautobot.core.forms import BootstrapMixin


# class RSSFeedForm(forms.ModelForm, BootstrapMixin):
#     """Form for creating or updating RSS feed configurations."""

#     class Meta:
#         model = RSSFeed
#         fields = ["name", "url"]
#         widgets = {
#             "name": forms.TextInput(attrs={"placeholder": "Enter feed name"}),
#             "url": forms.URLInput(attrs={"placeholder": "Enter feed URL"}),
#         }
