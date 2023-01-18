from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=255,blank=False)
    eroll_no = models.IntegerField(blank=False)
    departments = (
            ('CSE','CSE'),
            ('IT','IT'),
            ('ECE','ECE'),
            ('EEE','EEE'),
            ('Applied Science','Applied Science'),
            ('All','All'),
            ('None','None'),
        )
   
    Departments = models.CharField(max_length=255,choices=departments,blank=False,default="None")
    
    classOptions = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('IV','IV'),
    )
    
    Class = models.CharField(max_length=255,choices=classOptions)
    semester = models.IntegerField(blank=False)

    mobile_no = models.IntegerField(blank=False)
    mail_id = models.EmailField(blank=False)
    event_name = models.CharField(max_length=255,blank=False)
    type_of_event = (
        ('Cultural','Cultural'),
        ('Technical','Technical'),
        ('Sports','Sports'),
    )
    event_type = models.CharField(max_length=30,choices=type_of_event)
    event_date = models.DateField()
    organized_by = models.CharField(max_length=255)
    host_institute = models.CharField(max_length=255)
    position_obtained = (
        ('I','I'),
        ('II','II'),
        ('III','III'),
        ('Runner_up','Runner_up'),
    )

    position = models.CharField(max_length=20,choices = position_obtained)
    size_of_team = (
        ('Team','Team'),
        ('Individual','Individual'),
    )
    
    team_size = models.CharField(max_length=20,choices=size_of_team,blank= False) 
    level_of_comp = (
        ('College','College'),
        ('InterCollege','InterCollege'),
        ('University','University'),
        ('State','State'),
        ('National','National'),
        ('International','International'),
    )
    level = models.CharField(max_length=30,choices=level_of_comp,blank=False,default="College")
    date_of_award = models.DateField()
    upload_proof = models.CharField(max_length=255,blank=False)