from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet
from .models import Subscribers
class SubscriberViewSet(ModelViewSet):
    model = Subscribers #important
    icon = "mail"
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order =100
    add_to_admin_menu =True #important
    list_display = ("email" ,"fullname")
    search_fields = ("email" ,"fullname")
    form_fields = ("email", "fullname") #important

@hooks.register("register_admin_viewset")
def register_subscriber_viewset():
    return SubscriberViewSet("subscribers")