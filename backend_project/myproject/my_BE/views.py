from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset =Article.objects.select_related('author').all()
    serializer_class = ArticleSerializer
