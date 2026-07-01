from django.db import models
from django import forms
from django.shortcuts import render

from modelcluster.fields import ParentalKey ,ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
# Create your models here.
from wagtail.snippets.models import register_snippet
from wagtail.models import Page,Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import MultiFieldPanel ,FieldPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from wagtail.fields import StreamField
from streams import blocks
class BlogIndexPage(RoutablePageMixin,Page): 
    intro = RichTextField(blank=True)
    content = StreamField ([
        ("Title_and_Text",blocks.TitleAndTextBlock()), 
        ("RichText",blocks.RichTextBlock()), 
        ("SimpleRichText",blocks.SimpleRichTextBlock()),
        ("Cards", blocks.CardBlock()),
        ("Call_to_Action", blocks.CTABlock()),
        ("Single_button", blocks.ButtonBlock()),
    ],null=True,blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro"), FieldPanel("content")]
    def get_context(self ,request, *args , **kwargs): 
        context = super().get_context(request , *args , **kwargs)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['a_special_link'] = self.reverse_subpage('latest_posts')
        return context
    @route(r'^latest/?$', name="latest_posts")
    def latest_blog_post_with_top_5(self , request , *args , **kwargs):
        context = super().get_context(request , *args , **kwargs)
        context['latest_posts'] = BlogPage.objects.live().public()[:1]
        # context['name'] ="Anh o i i "
        # context['email'] = "anh.o.i.i@example.com"
        return render(request , "blog/latest_posts.html",context)
    def get_sitemap_urls(self,request):
        # if dont want to show in sitemap
        #return []
        sitemap = super().get_sitemap_urls(request)
        sitemap.append( {
            "location": self.full_url + self.reverse_subpage('latest_posts'), #name of the route   
            "lastmod": (self.last_published_at or self.latest_revision_created_at ),
        })
        return sitemap
    
class BlogTagIndexPage(Page):
    def get_context(self, request, *args, **kwargs):
        #filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        context = super().get_context(request, *args, **kwargs)
        context['blogpages']= blogpages
        return context
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage',
        related_name='tagged_items',on_delete=models.CASCADE)

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    # Add this
    authors = ParentalManyToManyField('blog.Author',blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag,blank=True)
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    content_panels = Page.content_panels + [
    MultiFieldPanel([
           FieldPanel("date"), FieldPanel("authors",widget=forms.CheckboxSelectMultiple), FieldPanel("tags")],heading="Blog information"),
           "intro","body","gallery_images"
           ]
class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage,on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        "image" , "caption"
    ]
@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image= models.ForeignKey(
        'wagtailimages.Image',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='+')
    panels = ["name","author_image"]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Authors"



