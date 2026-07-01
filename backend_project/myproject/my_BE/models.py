from django.db import models
from django.conf import settings
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, RichTextBlock
from wagtail.admin.panels import FieldPanel
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

class BlogPage(Page):
    template = "blog/blog_page.html"

    body = StreamField(
        [
            ("heading", CharBlock()),
            ("paragraph", RichTextBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]