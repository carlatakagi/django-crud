from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField('name',max_length=30)
  telephone = models.BigIntegerField('telephone')
  email = models.CharField('email',max_length=30)

  def __str__(self):
    return f"Name: {self.name}, Telephone: {self.telephone}, Email: {self.email}"