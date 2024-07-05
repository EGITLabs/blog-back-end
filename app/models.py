from django.db import models


class Post(models.Model):
    CATEGORY_CHOICES = [
        ("UNDERSTANDING_CONCEPTS", "Understanding Concepts in AI"),
        ("AI_IN_EDUCATION", "AI in Education"),
        ("AI_IN_NEWS", "AI in News/Trends"),
        ("SAFETY_AND_ETHICS", "Safety and Ethics of AI"),
    ]
    title = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=255, default="")
    content = models.TextField(default="")
    author = models.CharField(max_length=255, default="Omoro Rukevwe")
    snippet = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    category = models.CharField(
        max_length=255, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0]
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-").lower()
        super(Post, self).save(*args, **kwargs)
