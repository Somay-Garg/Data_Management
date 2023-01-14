from django.db import models

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
    name = models.CharField(max_length=100, blank=False)
    management = models.BooleanField(blank = False)
    yearofadmission = models.DateTimeField(blank=False)
    appno = models.CharField(blank=False, max_length=200)
    Fname = models.CharField(max_length=200, blank=False)
    Mname = models.CharField(max_length=200, blank=False)
    stream = models.CharField(max_length=200, choices= streamchoices,blank=False)
    DOB = models.DateField(blank=False)
    gender = models.CharField(max_length=50,choices= genderchoices ,blank=False)
    category = models.CharField(max_length=5,choices= categorychoices ,blank=False)
    subcategory = models.CharField(max_length=10, choices= subcategorychoices ,blank=False)
    region = models.CharField(max_length=50,choices= regionchoices ,blank=False)
    rank = models.IntegerField(null = True, default=None , blank=True)
    allottedquota = models.CharField(max_length=10,choices= allotedquotachoices, blank=False)
    allottedcategory = models.CharField(max_length=10,choices= allottedcategorychoices, blank=False)
    studentmobile = models.IntegerField(null = True, blank=True )
    emailid = models.EmailField(max_length=20, blank=False)
    fathermobile = models.IntegerField(null = True, default=None )
    address = models.CharField(max_length=200, blank=False)
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
    name = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=200, choices= streamchoices,blank=False)
    section = models.CharField(max_length=15,choices=sectionChoices,blank=False)
    passout = models.DateField(blank=False)
    is_placed = models.BooleanField(blank=False,default=False)
    appeared_for_exams = models.BooleanField(blank=False,default=False)
    current_status = models.CharField(max_length=50,blank=False,choices=statusChoices,default='Others')
    
    def _str_(self):
        return self.name

class StudentOfferDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    company_name = models.CharField(max_length=100, blank=False)
    package_in_lpa = models.IntegerField(default=None,blank=False)
    on_off_campus = models.CharField(max_length=15, default=None, blank=False)
    job_proof = models.CharField(max_length=255,blank=False)

    def _str_(self):
        return self.company_name

class StudentExamDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    exam_name = models.CharField(max_length=100, blank=False)
    exam_roll_no = models.BigIntegerField(default=None,blank=False)
    exam_date = models.DateField(blank=False)
    qualified = models.CharField(max_length=20, blank=False)
    score = models.IntegerField(default=None,blank=True ,null=True)
    rank = models.IntegerField(default=None,blank=True,null=True)
    date_of_result = models.DateField(blank=True,null=True)
    result_proof = models.CharField(max_length=255,blank=True,null=True)

    def _str_(self):
        return self.exam_name

class StudentCurrentStatusJobDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    company_name = models.CharField(max_length=100, blank=False)
    date_of_joining = models.DateField(blank=False)
    address = models.CharField(max_length=255, blank=False)
    joining_proof = models.CharField(max_length=255,blank=True)

    def _str_(self):
        return self.company_name

class StudentCurrentStatusHighEduDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    college_name = models.CharField(max_length=100, blank=False)
    course_name = models.CharField(max_length=100, blank=False)
    country_name = models.CharField(max_length=100, blank=False)
    college_address = models.CharField(max_length=255, blank=False)
    id_proof = models.CharField(max_length=255,blank=True)

    def _str_(self):
        return self.college_name

class StudentCurrentStatusEntrepreDetails(models.Model):
    enrollmentno = models.IntegerField(null = True, default=None , blank=False)
    startup_name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=255, blank=False)
    startup_country = models.CharField(max_length=100, blank=False)
    sector = models.CharField(max_length=100, blank=False)
    website = models.URLField(max_length=200)

    def _str_(self):
        return self.startup_name
