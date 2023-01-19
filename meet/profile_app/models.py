from django.db import models




ORIENTATION_CHOICES = [
    ('MAN', 'Man'),
    ('WOMAN', 'Woman'),
    ('BI', 'Bi'),
    ('OTHER', 'Other')
]

GENDER_CHOICES = [
    ('MALE', 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
    ]

class Questionnaire(models.Model):
    nickname = models.CharField(max_length=20, blank=True, verbose_name='Nickname')
    name = models.CharField(max_length=20, blank=True, null=True verbose_name='Name')
    surname = models.CharField(max_length=20, blank=True, null=True verbose_name='Surname')
    birthday = models.DateField(auto_now = False , auto_now_add = False )
    orientation = models.CharField(choices=ORIENTATION_CHOICES)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES)
    phone = models.IntegerField(blank=True, max_length=20)
    user = models.OneToOneField('User', related_name='questionnaire')
    
class User(models.Model):


class Photo(models.Model):
    image = models.ImageField(upload_to = None , height_field = None , width_field = None , max_length = 100)
    questionnaire = 