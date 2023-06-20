from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

User = get_user_model()

# Category
    # name
class Category(models.Model):
    name = models.CharField(_("name"), max_length=50)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


# NewsArticle
    # title
    # description
    # source_url
    # image
    # published_at
    # category (FK Category (Many to Many))
class NewsArticle(models.Model):
    title = models.CharField(_("title"), max_length=100)
    description = models.TextField(_("description"), max_length=250)
    source_name = models.TextField(_("source_name"), max_length=50)
    source_url = models.URLField(_("source_url"), max_length=300)
    image = models.URLField(_("image"), max_length=400)
    published_at = models.DateTimeField(_("published_at"))
    category = models.ManyToManyField(
        Category,
        verbose_name=_("category"),
        related_name="articles",
    )

    class Meta:
        verbose_name = _("news article")
        verbose_name_plural = _("news articles")

    def __str__(self):
        return f"{self.title} {self.source_name} {self.published_at}"

    def get_absolute_url(self):
        return reverse("newsarticle_detail", kwargs={"pk": self.pk})
    
    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])
    
    display_category.short_description = 'Category'


# Comment
    # article (FK NewsArticle (One to Many))
    # user (FK User (One to Many))
    # content
    # created_at
class Comment(models.Model):
    article = models.ForeignKey(
        NewsArticle,
        verbose_name=_("article"),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField(_("content"), max_length=5000)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)

    class Meta:
        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return f"{self.user} {self.created_at}"

    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})




