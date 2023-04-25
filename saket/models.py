from django.db import models

# Create your models here.

ARTS = 'ARTS'
COMMERS = 'COMMERS'
COMMERS_PLUS_MATHS = 'COMMERS+MATHS'
SCIENCE = 'SCIENCE'
A1 = 'B.A'
C1 = 'B.M.S'
C2 = 'B.COM'
S1 = 'BscIT'
S2 = 'BscCS'
CS1 ='BscIT'
CS2 ='B.M.S'
CS3 ='B.COM'
d = 'Download'
a = 'Apply'

SUBJECT_CHOICES = [
    (SCIENCE, SCIENCE),
    (COMMERS, COMMERS),
    (COMMERS_PLUS_MATHS, COMMERS_PLUS_MATHS),
    (ARTS, ARTS),
]

JOB_CHOICES = [
    (S1, S1),
    (S2, S2),
    (C1, C1),
    (C2, C2),
    (CS1, CS1),
    (CS2, CS2),
    (CS3, CS3),
    (A1, A1)

]

but_Choices = [
    (d,d),
    (a,a)
]

def get_cs_strings():
    cs_strings = [
        CS1,
        CS2,
        CS3,
    ]

    return cs_strings


def get_c_strings():
    c_strings = [
        C1,
        C2,
    ]

    return c_strings

def get_a_strings():
    a_strings = [
        A1,
    ]

    return a_strings

def get_s_strings():
    s_strings = [
        S1,
        S2,
    ]

    return s_strings

class Person(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    p_no = models.CharField(max_length=10)
    email = models.EmailField(max_length=50,null=True)
    persontage = models.IntegerField(null=True, blank=True)
    # id_maths_marks
    maths_marks = models.IntegerField(null=True, blank=True)
    # id_subject
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    # id_deg
    deg = models.CharField(max_length=50, choices=JOB_CHOICES)
    documents = models.FileField(upload_to='media/',null=True,blank=True)


class NewEvent(models.Model):
    pho = models.ImageField(upload_to='media/', null=True, blank=True)
    title = models.CharField(max_length=50)
    post_time = models.TimeField(max_length=50)
    post_date = models.DateField(max_length=50)
    sub = models.CharField(max_length=50)
    dis = models.TextField(max_length=10000)
    event_time = models.TimeField(max_length=50,null=True, blank=True)
    event_date = models.DateField(max_length=50,null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    button = models.CharField(max_length=200, choices=but_Choices, null=True, blank=True)

class News(models.Model):
    pho = models.ImageField(upload_to='media/')
    new_type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    post_time = models.TimeField(max_length=50)
    post_date = models.DateField(max_length=50)
    quote = models.TextField(max_length=50)
    dis = models.TextField(max_length=10000)



class Courses_for_arts(models.Model):
    pho = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    fid = models.CharField(max_length=100)
    deg_name = models.CharField(max_length=100)
    dis = models.TextField(max_length=1000)

class Courses_for_sci(models.Model):
    pho = models.ImageField(upload_to='media/')
    fid = models.CharField(max_length=100)
    deg_name = models.CharField(max_length=100)
    dis = models.TextField(max_length=1000)

class Courses_for_commersPlusMaths(models.Model):
    pho = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    fid = models.CharField(max_length=100)
    deg_name = models.CharField(max_length=100)
    dis = models.TextField(max_length=1000)

class Courses_for_commers(models.Model):
    pho = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100)
    fid = models.CharField(max_length=100)
    deg_name = models.CharField(max_length=100)
    dis = models.TextField(max_length=1000)

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    email = models.EmailField()


