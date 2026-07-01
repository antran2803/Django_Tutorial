from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(blank=True, null=True, help_text="Facebook channel")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter channel")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube channel")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
        ],heading = "Social Media Settings")
    ]

@register_setting
class ContactSettings(BaseSiteSetting):
    contact_email = models.EmailField(blank=True, null=True, help_text="Contact email address")
    contact_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number")
    contact_address = models.TextField(blank=True, null=True, help_text="Contact address")

    panels = [
        MultiFieldPanel([
            FieldPanel("contact_email"),
            FieldPanel("contact_phone"),
            FieldPanel("contact_address"),
        ], heading="Contact Settings")
    ]