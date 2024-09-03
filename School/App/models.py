from django.db import models
from django.utils import timezone

# Create your models here.
class techlog(models.Model):
          staffid=models.CharField(max_length=30)
          password=models.CharField(max_length=30)
          
          def __str__(self):
                  return self.staffid
          
          
statusChoice = (
    ('Present','Present'),
    ('Absent','Absent')
)
class createAttendance(models.Model):
    roll_no = models.IntegerField()
    studName = models.CharField(max_length=50)
    studDept = models.CharField(max_length=50)
    studPeriod =models.CharField(max_length=50)
    status = models.CharField(max_length=50,choices=statusChoice)
    # dailyDate = models.DateTimeField(default=timezone.now)
    date=models.DateField()
    time=models.TimeField()
    percentage = models.FloatField()
    # time = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.studName
    
class attendance(models.Model):
     roll_no=models.CharField(max_length=20)
     subject=models.CharField(max_length=100)
     status=models.CharField(max_length=10)
    #  subject=models.CharField(max_length=20)

     def __str__(self):
          return self.roll_no
    
class StuMark(models.Model):
    S_name=models.CharField(max_length=30)
    S_roll=models.CharField(max_length=30)
    S_dep=models.CharField(max_length=30)
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()    
    science=models.IntegerField()
    social=models.IntegerField()
    total=models.IntegerField()
    per=models.FloatField()
    grade=models.CharField(max_length=30)
    staffid = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.S_name

class Sregister(models.Model):
    sname=models.CharField(max_length=50)
    email=models.EmailField()
    stuid=models.CharField(max_length=10)
    passw=models.CharField(max_length=50)

    def __str__(self):
        return self.sname

class Feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
         return self.name

class Motivate(models.Model):
    title=models.CharField(max_length=100)
    motivate=models.TextField()

    def __str__(self):
         return self.motivate
    
class Announcement(models.Model):
    announcement=models.TextField()

