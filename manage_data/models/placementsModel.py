from django.db import models
# from django.conf import settings
# Create your models here.

allotedquotachoices = (
    ('opno','OPNO'),
    ('scno', 'SCNO'),
    ('stno','STNO'),
    ('nodf','NODF'),
    ('noph','NOPH'),
)

allottedcategorychoices = (
    ('hs', 'HS'),
    ('os', 'OS'),
    ('ai', 'AI'),
)

subcategorychoices = (
    ('defence','DEFENCE'),
    ('jain', 'JAIN'),
    ('muslim','MUSLIM'),
    ('sikh','SIKH'),
    ('pwd','PWD'),
    ('jk','JK'),
)

regionchoices = (
    ('delhi', 'DELHI'),
    ('outside delhi', 'OUTSIDE DELHI'),
)

categorychoices = (
    ('gen', 'GEN'),
    ('sc', 'SC'),
    ('st', 'ST'),
    ('obc', 'OBC'),
    ('ews', 'EWS'),
    ('aicte', 'AICTE'),
)

genderchoices = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other', 'OTHER'),
)

typechoices = (
    ('regular', 'REGULAR'),
    ('upgraded', 'UPGRADED'),
    ('le', 'LE'),
)

streamchoices = (
    ('cse','CSE'),
    ('it','IT'),
    ('ece','ECE'),
    ('eee','EEE'),
)

class Student(models.Model):
    type = models.CharField(max_length=10, choices= typechoices ,default='Regular')
    enrollmentno = models.IntegerField(null = True, default=None , blank=True)
    name = models.CharField(max_length=100, default=False)
    management = models.BooleanField(default = False)
    yearofadmission = models.DateTimeField(default=False)
    appno = models.CharField(default=False, max_length=200)
    Fname = models.CharField(max_length=200, default=False)
    Mname = models.CharField(max_length=200, default=False)
    stream = models.CharField(max_length=200, choices= streamchoices,default=False)
    DOB = models.DateField(default=False)
    gender = models.CharField(max_length=50,choices= genderchoices ,default=False)
    category = models.CharField(max_length=5,choices= categorychoices ,default=False)
    subcategory = models.CharField(max_length=10, choices= subcategorychoices ,default=False)
    region = models.CharField(max_length=50,choices= regionchoices ,default=False)
    rank = models.IntegerField(null = True, default=None , blank=True)
    allottedquota = models.CharField(max_length=10,choices= allotedquotachoices, default=False)
    allottedcategory = models.CharField(max_length=10,choices= allottedcategorychoices, default=False)
    studentmobile = models.IntegerField(null = True, default=None , blank=True)
    emailid = models.EmailField(max_length=20, default=False)
    fathermobile = models.IntegerField(null = True, default=None , blank=True)
    address = models.CharField(max_length=200, default=False)
    aggregate = models.FloatField(null = True, default=None , blank=True)
    pcm = models.FloatField(null = True, default=None , blank=True)

    def _str_(self):
        return self.name
    def yearpub(self):
        return self.yearofadmission.strftime('%Y')

    def dateofbirth(self):
        return self.DOB.strftime('%d-%m-%Y')

sectionChoices = (
    ('I','I'),
    ('II','II'),
    ('III','III'),
    ('IV','IV'),
    ('All','All'),
)

statusChoices = (
    ('Job','Job'),
    ('Higher Education','Higher Education'),
    ('Entreprenurship','Entreprenurship'),
    ('Others','Others'),
)

class StudentPlacement(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=True)
    name = models.CharField(max_length=100, default=False)
    department = models.CharField(max_length=200, choices= streamchoices,default=False)
    section = models.CharField(max_length=15,choices=sectionChoices,default=False)
    passout = models.DateField(default=False)
    is_placed = models.BooleanField(blank=False,default=False)
    appeared_for_exams = models.BooleanField(blank=False,default=False)
    current_status = models.CharField(max_length=20,blank=False,choices=statusChoices,default=None)
    
    def _str_(self):
        return self.name

class StudentOfferDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    company_name = models.CharField(max_length=100, default=False)
    package_in_lpa = models.IntegerField(default=None,blank=False)
    on_off_campus = models.CharField(max_length=5, default=None, blank=False)
    job_proof = models.CharField(max_length=255,blank=False)

    def _str_(self):
        return self.company_name

class StudentExamDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    exam_name = models.CharField(max_length=100, default=False)
    exam_roll_no = models.BigIntegerField(default=None,blank=False)
    exam_date = models.DateField(default=False)
    qualified = models.CharField(max_length=20, default=False)
    score = models.IntegerField(default=None,blank=True)
    rank = models.IntegerField(default=None,blank=True)
    result_proof = models.CharField(max_length=255,blank=True)

    def _str_(self):
        return self.exam_name

class StudentCurrentStatusJobDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    company_name = models.CharField(max_length=100, default=False)
    date_of_joining = models.DateField(blank=False)
    address = models.CharField(max_length=255, default=False)
    joining_proof = models.CharField(max_length=255,blank=True)

    def _str_(self):
        return self.company_name

class StudentCurrentStatusHighEduDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    college_name = models.CharField(max_length=100, default=False)
    course_name = models.CharField(max_length=100, default=False)
    country_name = models.CharField(max_length=100, default=False)
    id_proof = models.CharField(max_length=255,blank=True)

    def _str_(self):
        return self.college_name

class StudentCurrentStatusEntrepreDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    startup_name = models.CharField(max_length=100, default=False)
    address = models.CharField(max_length=255, default=False)
    sector = models.CharField(max_length=100, default=False)
    website = models.URLField(max_length=200)

    def _str_(self):
        return self.startup_name

otherChoices = (
    ('Preparing for Entrance Exams','Preparing for Entrance Exams'),
    ('Family Business','Family Business'),
)

class StudentCurrentStatusOtherDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    other = models.CharField(max_length=40,default=None,blank=True)

    def _str_(self):
        return self.other
