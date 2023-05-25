from django.db import models

class Book(models.Model):
    title = models.CharField(100)
    author = models.CharField(50)
    pub_date = models.DateField()

    def __str__(self):
        return self.title