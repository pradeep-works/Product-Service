from django.db import models

# Create your models here.
class Base(models.Model):
    '''
    Base Model for all retest_app models
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Product(Base):
    '''
    Captures Product information
    '''
    name = models.CharField(max_length=16, db_index=True)
    price = models.FloatField()
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()