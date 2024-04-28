from django.db import models

class Country123(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class Meta:
        db_table = "country123"

class Kid123(models.Model):
    Name = models.CharField(max_length=100)
    Sex = models.CharField(max_length=2)
    Country = models.ForeignKey('Country123', related_name='kid', on_delete=models.CASCADE)
    Missing_Since = models.CharField(max_length=100)
    Missing_From = models.CharField(max_length=100)
    Nationality = models.CharField(max_length=30)
    Height = models.IntegerField(null=True)
    Weight = models.IntegerField(null=True)
    Age = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.Name

class Meta:
        db_table = "kid123"

