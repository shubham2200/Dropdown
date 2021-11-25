from django.db import models

# Create your models here.



class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class state(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class city(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name





class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(state, on_delete=models.SET_NULL, blank=True, null=True)
    city =  models.ForeignKey(city, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
