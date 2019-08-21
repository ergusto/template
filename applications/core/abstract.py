from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class AbstractTimestampedModel(models.Model):
    created = models.DateTimeField(blank=True, null=True, editable=False)
    modified = models.DateTimeField(blank=True, null=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.id:
            self.created = now
        else:
            self.modified = now
        super(AbstractTimestampedModel, self).save(*args, **kwargs)

class AbstractSluggableModel(models.Model):
    slug = models.SlugField(max_length=280, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.title and not self.id:
            self.slug = slugify(self.title)
        super(AbstractSluggableModel, self).save(*args, **kwargs)
