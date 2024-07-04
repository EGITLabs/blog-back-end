from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, default="")
    content = models.TextField(default="")
    author = models.CharField(max_length=255, default="Omoro Rukevwe")
    snippet = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name
