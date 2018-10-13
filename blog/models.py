from django.db import models
from django.utils import timezone
from django.urls import reverse

# BlogPost model
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        name = 'post-detail'
        args = [self.pk]
        return reverse(name,args=args)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
