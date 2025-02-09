from django.db import models
from django.utils import timezone

CHAI_TYPE_CHOICES = [
    ('ML','MASALA'),
    ('GR','GINGER'),
    ('KL','KIWI'),
    ('PL','PLAIN'),
    ('EL','ELAICHI')
]

# Create your models here.
class ChaiVariety(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

