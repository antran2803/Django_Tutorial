from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.models import Page ,Orderable
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField

from streams import blocks
from subscribers.models import Subscribers

class HomePageCarouselImages(Orderable):
    page = ParentalKey("home.HomePage",related_name="carousel_images")
    carousel_images = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        FieldPanel("carousel_images"),
    ]
class HomePage(RoutablePageMixin,Page):
    template = "home/home_page.html"
    max_count = 1
    content_details = models.CharField(max_length=100,blank=False,null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.ForeignKey (
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField([
        ("Call_to_Action", blocks.CTABlock()),
    ], null=True, blank=True)

    
    content_panels = Page.content_panels + [
        FieldPanel("content_details"),
      MultiFieldPanel([
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        FieldPanel("banner_cta"),
        ], heading="Banner Options"),
        MultiFieldPanel([
        InlinePanel("carousel_images", max_num=5, min_num=1 , label="Carousel Images"),

        ] , heading="Carousel Images"),
        FieldPanel("content"),
        
    ]
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
    
    @route(r'^subscribe/$')
    def the_subscribe_page(self,request ,*args , **kwargs):
        context = super().get_context(request, *args, **kwargs)
        subscribers = Subscribers.objects.all()
        context['subscribers'] = subscribers
        return render(request, "home/subscribe.html", context)





