from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()


#Person.objects.get_or_create(name='online',number=3)
#Person.objects.create(name='online', number=2)

#p = Person(name='sended', number=23)
#p.save()

# Create your models here.
