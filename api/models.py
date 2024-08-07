from django.db import models

# Create your models here.

#Company model
class Company(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ('Mobile phones','Mobile phones')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' -- '+ self.location    

#Employee model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    desingnation=models.CharField(max_length=50, choices=(
        ('Manager','Manager',),
        ('Software Developer','Software Developer'),
        ('Project Leader','PL')
        ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE) #we can identify which emp is from which company with this relation
