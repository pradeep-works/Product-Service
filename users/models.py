from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
# Create your models here.

class Base(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class UserGroup(Base):
    '''
    Model to Create Auth Group
    '''
    name = models.CharField(max_length=32, unique=True)
    
    def save(self, *args, **kwargs):
        # print(self._state.adding)
        group, created = Group.objects.get_or_create(name=self.name)
        return super().save(*args, **kwargs)

class User(AbstractUser, Base):
    '''
    Captures the User information
    '''
    display_name = models.CharField(max_length=32, db_index=True)