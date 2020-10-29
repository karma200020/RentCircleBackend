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
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    posted_on = models.DateField(null=False)
    item = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    item_count = models.PositiveSmallIntegerField()
    category = models.CharField(choices=categories,max_length=20)
    contact_number = models.CharField(max_length=15)
    contact_email = models.EmailField()
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    # images = ArrayField(models.ImageField, null=True, name='images')
