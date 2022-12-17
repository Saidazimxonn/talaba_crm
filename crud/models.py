from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('Ism',max_length=255, help_text='Ali')
    talab_raqami = models.IntegerField()
    l_name = models.CharField('Familya', max_length=255, help_text='Aliyev')
    age = models.IntegerField('Yoshi', help_text='25')
    country = models.CharField('Vatani', max_length=255 , help_text='China')
    region  = models.CharField('Viloyat', max_length=255, help_text='Samarqand')
    group  = models.IntegerField('Guruh')

    def __str__(self):
        return f'{self.name} {self.l_name} '


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    number = models.IntegerField(min=3)

    def __str__(self):
        return self.group_name

class Subject(models.Model):
    s_name = models.CharField(max_length=255)
    raqami = models.IntegerField()

    def __str__(self):
        return self.s_name