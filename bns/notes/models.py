from django.db import models


# Create your models here.

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class AllNotes(models.Model):
    notes_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title
