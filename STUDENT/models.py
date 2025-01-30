from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


program_list=(
('Bachelor Commerce in Procurement and Logistics Management','Bachelor Commerce in Procurement and Logistics Management'),
('Bachelor of Arts in Cultural Heritage and Tourism','Bachelor of Arts in Cultural Heritage and Tourism'),
('Bachelor of Arts in Development Studies','Bachelor of Arts in Development Studies'),
('Bachelor of Arts in Economics','Bachelor of Arts in Economics'),
('Bachelor of Arts in Economics and Sociology','Bachelor of Arts in Economics and Sociology'),
('Bachelor of Arts in Economics and Statistics','Bachelor of Arts in Economics and Statistics'),
('Bachelor of Arts in English','Bachelor of Arts in English'),
('Bachelor of Arts in Environmental Disaster Management','Bachelor of Arts in Environmental Disaster Management'),
('Bachelor of Arts in Environmental Economics and Policy','Bachelor of Arts in Environmental Economics and Policy'),
('Bachelor of Arts in Fine Arts and Design','Bachelor of Arts in Fine Arts and Design'),
('Bachelor of Arts in French','Bachelor of Arts in French'),
('Bachelor of Arts in Geography and Environmental Studies','Bachelor of Arts in Geography and Environmental Studies'),
('Bachelor of Arts in History','Bachelor of Arts in History'),
('Bachelor of Arts in International Relations','Bachelor of Arts in International Relations'),
('Bachelor of Arts in Kiswahili Lingustics','Bachelor of Arts in Kiswahili Lingustics'),
('Bachelor of Arts in Kiswahili Literature','Bachelor of Arts in Kiswahili Literature'),
('Diploma in Computer Networks','Diploma in Computer Networks'),
('Diploma in Computer Systems Administration','Diploma in Computer Systems Administration'),
('Diploma in Cultural Heritage and Tourism','Diploma in Cultural Heritage and Tourism'),
('Diploma in Early Childhood Education','Diploma in Early Childhood Education'),
('Diploma in Educational Technology','Diploma in Educational Technology'),
('Diploma in Film Production','Diploma in Film Production'),
('Diploma in Forensic Sciences','Diploma in Forensic Sciences'),
('Diploma in Forest Management and Nature Conservation','Diploma in Forest Management and Nature Conservation'),
('Diploma in GIS and Remote Sensing','Diploma in GIS and Remote Sensing'),
('Diploma in Graphic Design and Web Technology','Diploma in Graphic Design and Web Technology'),
('Diploma in ICT with Education','Diploma in ICT with Education'),
('Diploma in Information and Telecommunication Technology','Diploma in Information and Telecommunication Technology'),
('Diploma in Information Technology Management','Diploma in Information Technology Management'),
('Diploma in Marketing','Diploma in Marketing'),
('Diploma in Mass Communication','Diploma in Mass Communication'),
('Diploma in Medical Laboratory Science','Diploma in Medical Laboratory Science'),
('Diploma in Mineral Exploration in Mining Geology','Diploma in Mineral Exploration in Mining Geology'),
('Diploma in Mining Engineering','Diploma in Mining Engineering'),
('Diploma in Multimedia and Animation Technology','Diploma in Multimedia and Animation Technology'),
('Diploma in Nursing','Diploma in Nursing'),
('Diploma in Pharmacy','Diploma in Pharmacy'),
('Diploma in Primary Teacher Education','Diploma in Primary Teacher Education'),
('Diploma in Procurement and Logistics Management','Diploma in Procurement and Logistics Management'),
('Diploma in Project Planning and Management','Diploma in Project Planning and Management'),
('Diploma in Public Administration and Management','Diploma in Public Administration and Management'),
('Diploma in Renewable Energy Engineering','Diploma in Renewable Energy Engineering'),
('Diploma in Social Work and Community Development','Diploma in Social Work and Community Development'),
('Diploma in Statistics','Diploma in Statistics'),
('Diploma in Telecommunication Nerworks','Diploma in Telecommunication Nerworks'),
('Diploma in Tourism and Management','Diploma in Tourism and Management'),
('Stashahada ya Kiswahili','Stashahada ya Kiswahili'),

)

class Student(models.Model):
     id=models.AutoField(primary_key=True)
     program=models.CharField(max_length=250,choices=program_list)
     student_id=models.ForeignKey(User,on_delete=models.CASCADE)

class Books(models.Model):
     id=models.AutoField(primary_key=True)
     logo=models.ImageField(upload_to="logo/")
     file=models.FileField(upload_to="pdf")
     heading=models.CharField(max_length=200)
     description=RichTextField(blank=True,null=True)
     book_name=models.CharField(max_length=200)
     author=models.CharField(max_length=200)
     publication_year=models.DateTimeField()
     isbn=models.IntegerField()
     date=models.DateTimeField(auto_now_add=True)
     program=models.CharField(max_length=250,choices=program_list)

