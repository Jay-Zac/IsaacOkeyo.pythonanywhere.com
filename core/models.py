from django.db import models


class Work(models.Model):
    objects = None
    image = models.ImageField(upload_to='my_works_images', null=False, blank=False)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=2083)
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Complete(models.Model):
    objects = None
    number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'complete_works'

    def __int__(self):
        return self.number


class HappyCustomer(models.Model):
    objects = None
    number = models.IntegerField()

    class Meta:
        verbose_name_plural = 'happy_customers'

    def __int__(self):
        return self.number


class Skill(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.title
