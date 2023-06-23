from typing import Any
from news_aggregator_app.models import NewsArticle
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        NewsArticle.objects.all().delete()