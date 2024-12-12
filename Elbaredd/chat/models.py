from django.db import models


class User_name(models.Model):
    user_text = models.CharField(max_length=200)


class messages(models.Model):
        identifier = models.CharField(max_length=200)
        sender = models.CharField(max_length=200)
        reciever = models.CharField(max_length=200)
        message = models.CharField(max_length=200)