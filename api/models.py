from django.db import models

# Create your models here.
class User(models.Model):
    company_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    EmployeeID=models.CharField(max_length=40 )
    Status=models.CharField(max_length=100,choices=(('Active','Active'),('Non-active','Non-active')))
    Email=models.CharField(max_length=50)
    Token=models.CharField(max_length=20)
    Token_Expires_at = models.DateTimeField()
    Role = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    Team = models.CharField(max_length=80 , choices=(('Engineering','Engineering'),('Marketing','Marketing'),('Hr','Hr')))
    Batch=models.CharField(max_length=100,choices=(('2020','2020',),('2021','2021'),('2022','2022')))
    Shifts=models.CharField(max_length=70,default='N/A',choices=(('Morning','Morning'),('Night','Night')))
    # locaction=models.CharField(max_length=50)
    # # about=models.TextField()
    type=models.CharField(max_length=100,default='N/A' ,choices=(('IT','IT'),('Non IT','Non It',),('Mobiles Phones','Mobiles Phones')))
    added_date=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name 
class Empid(models.Model):
   
    name= models.CharField(max_length=50)
    type=models.CharField(max_length=20)


    #employee Model
class AddLeave(models.Model):
    Username=models.ForeignKey(User, on_delete=models.CASCADE)
    Employeeid=models.ForeignKey(Empid, on_delete=models.CASCADE)
    LeaveType=models.CharField(max_length=100)
    LeaveBalance=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    From=models.DateTimeField(max_length=10)
    ToDate=models.DateTimeField()
    Duration=models.CharField(max_length=50)
    AppliedTo=models.CharField(max_length=50)
    Notes=models.CharField(max_length=50)
    LeaveStatus=models.CharField(max_length=50,choices=(
        ('Approved','Approved'),
        ('Rejected','Rejected'),
        ('Pending','Pending'),
        ('Cancelled','Cancelled')
    ))

   
    # empid=  models.ForeignKey(Empid, on_delete=models.CASCADE)  