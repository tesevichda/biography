from django.db import models
from django.utils import timezone


class Document(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    document_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Person: {} {}>".format(self.title, self.document_date)


class Person(models.Model):
    MALE = 'ML'
    FEMAIL = 'FM'

    GENDER_TYPES = (
        (MALE, 'мужской'),
        (FEMAIL, 'женский')
    )

    first_name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    snils = models.CharField(max_length=14, null=True)
    passport = models.CharField(max_length=11, null=True)
    father = models.ForeignKey('self', null=True, related_name='father_child', on_delete=models.CASCADE)
    mother = models.ForeignKey('self', null=True, related_name='mother_child', on_delete=models.CASCADE)
    birth_date = models.DateTimeField(default=timezone.now)
    gender = models.CharField(max_length=7, choices=GENDER_TYPES)
    email = models.CharField(max_length=200) #
    mobile = models.CharField(max_length=200) #
    educations = models.ManyToManyField('Education', through='Pupil')
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Person: {} {}>".format(self.surname, self.first_name)


class Education(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Education: {} {}>".format(self.name, self.address)


class Pupil(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s is/was in education %s (from %s till %s)" % (self.person, self.education, self.start_date, self.finish_date)


class Event(models.Model):
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "<Event: {} {}>".format(self.title, self.event_date)
