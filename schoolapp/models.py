from django.db import models
from django.urls import reverse 



    
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def __str__(self):
        return self.name
def get_absolute_url(self):
        return reverse('department_detail', args=[str(self.id)])
    
class Material(models.Model):
  
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
   
    
 
class Order(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=gender_choices)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose_choices = [
        ('enquiry', 'For Enquiry'),
        ('place_order', 'Place Order'),
        ('return', 'Return'),
    ]
    purpose = models.CharField(max_length=20, choices=purpose_choices)
    materials_provided = models.ManyToManyField(Material)

    def __str__(self):
        return self.name