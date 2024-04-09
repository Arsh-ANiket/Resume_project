from django.db import models

# Create your models here.
class Organizations(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    city=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Candidates(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    # education
    tenth_school=models.CharField(max_length=100)
    tenth_year=models.CharField(max_length=100)
    tenth_marks = models.DecimalField(max_digits=5, decimal_places=2)
    twelfth_school=models.CharField(max_length=100)
    twelfth_year = models.CharField(max_length=100)
    twelfth_marks = models.DecimalField(max_digits=5, decimal_places=2)
    #technical
    skill1=models.CharField(max_length=20)
    skill2=models.CharField(max_length=20)
    skill3=models.CharField(max_length=20)
    interested_position_choices = [
        ('position1', 'Software Engineer'),
        ('position2', 'Data Analyst'),
        ('position3', 'Data Engineer'),]
    interested_position=models.CharField(max_length=20,choices=interested_position_choices)
    
    resume=models.FileField(upload_to='resumes/', null=True,blank=True )

    def __str__(self):
        return self.name