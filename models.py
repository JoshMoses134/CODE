from django.db import models
from sqlite3 import Date

# Create your models here.
class Person(models.Model):
    First_Name=models.CharField(help_text="First Name", max_length=50)
    Last_Name=models.CharField(help_text="Last Name", max_length=50)
    Email=models.EmailField(help_text="Email", unique=True, max_length=50)
    DOB= models.DateField(default=Date.today)
    Phone_Number= models.CharField(help_text="Phone Number", unique=True, max_length=50)
    Residential_Address=models.CharField(help_text="Address", max_length=50)
    Emergency_Contact= models.CharField(help_text='Emergency Contact', max_length=30)
    Programme= (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time')
    )
    Department=(
        ('Microbiology', 'Microbiology'),
        ('Physics', 'Physics'),
        ('Animal And Environmental Biology', 'Animal And Environmental Biology'),
        ('Computer Science', 'Computer Science'),
        ('Botany', 'Botany'),
        ('Chemistry', 'Chemistry'),
        ('Mathematics','Mathematics'),
        ('Statistics', 'Statistics'),
        ('Computer Science', 'Computer Science'),
        ('Biochemistry', 'Biochemistry')
    )
    Session=(
        ('2021/2022', '2021/2022'),
        ('2020/2021', '2020/2021'),
        ('2019/2020', '2019/2020'),
        ('2018/2019', '2018/2019'),
        ('2017/2018', '2017/2018'),
        ('2016/2017', '2016/2017'),
        ('2015/2016', '2015/2016'),
        ('2014/2015', '2014/2015'),
        ('2013/2014', '2013/2014'),
        ('2012/2013', '2012/2013'),
        ('2011/2012', '2011/2012'),
    )
    session= models.CharField(help_text='Session', choices=Session, null=True, max_length=70)
    department= models.CharField(help_text='Department', choices=Department, null=True, max_length=70)
    programme= models.CharField(help_text='Programme', choices=Programme, null=True, max_length=70)

    class Meta:
        abstract= True

class Student(Person):
    Matric_Number = models.CharField(max_length=50, default='10/CO/SC/100', help_text='Matric Number')
        
    class Meta:
        ordering= ['First_Name']

    def __str__(self):
        return f'{self.First_Name}'

class Lecturer(Person):
    Staff= (
        ('Teaching Staff', 'Teaching Staff'),
        ('Non-Teaching Staff', 'Non-Teaching Staff')
    )
    staff= models.CharField(max_length=50, choices=Staff, help_text='Staff')

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'

class Student_Bio_Data(models.Model):
    Name= models.ForeignKey(Student,on_delete=models.CASCADE)
    Other_Contacts= models.CharField(help_text='Other Contact', default='090354536778', max_length=14)
    Description=models.TextField(help_text='Short Description About Yourself')
    Date_Uploaded= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Students' Bio_Data"

    def __str__(self):
        return f'Last Updated: {self.Date_Uploaded}'




    