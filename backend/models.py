import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.


class post(models.Model):
    categories = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c')
    )
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)
    posted_on = models.DateField(null=False)
    item = models.CharField(max_length=40)
    rating = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    item_count = models.PositiveSmallIntegerField()
    category = models.CharField(choices=categories, max_length=20)
    contact_number = models.CharField(max_length=15)
    cost = models.IntegerField(default=0)
    contact_email = models.EmailField()
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    productId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # images = ArrayField(models.ImageField, null=True, name='images')

    def __str__(self):
        return self.item


class review(models.Model):
    reviewer = models.ForeignKey(User, related_name='reviewer', on_delete=models.CASCADE)
    item = models.ForeignKey(post, related_name='reviewed', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.reviewer.first_name + ' -  ' + self.item.item




