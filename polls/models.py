from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    #dob = models.DateField() #year-month-date

    #restaurant = models.ForeignKey(Restaurant)
    # dish = models.ForeignKey(Dish)

    #what if i dont want to fill from admin and want no answer?
    #dish = models.ForeignKey(Dish, blank=True, null=True)
    #WHY ADMIN LET ME CHOSSE ANY DISH, should be showing just the dish of the restaurant???

    def __str__(self):
        return self.name + self.last_name


class Choice(models.Model):
    person = models.ForeignKey(Person)
    restaurant_vote = models.ForeignKey(Restaurant, related_name="res_vote")

    date_vote = models.DateField(null=True, blank=True)
    time_vote = models.TimeField(null=True, blank=True)

    restaurant_winner = models.ForeignKey(Restaurant, null=True, blank=True, related_name="res_winner")
    dish = models.ForeignKey(Dish, null=True, blank=True)
    time_dish = models.TimeField(null=True, blank=True)
    def __str__(self):
        return str(self.person.name)+" "+str(self.person.last_name) + " choose " + str(self.restaurant_vote)