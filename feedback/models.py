from django.db import models

# Create your models here.
class FeedbackCsn211(models.Model):
    sid = models.IntegerField(primary_key=True)
    q1 = models.IntegerField(blank=True, null=True)
    q2 = models.IntegerField(blank=True, null=True)
    q3 = models.IntegerField(blank=True, null=True)
    q4 = models.IntegerField(blank=True, null=True)
    q5 = models.IntegerField(blank=True, null=True)
    q6 = models.IntegerField(blank=True, null=True)
    q7 = models.IntegerField(blank=True, null=True)
    q8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_csn211'



class FeedbackCsn209(models.Model):
    sid = models.IntegerField(primary_key=True)
    q1 = models.IntegerField(blank=True, null=True)
    q2 = models.IntegerField(blank=True, null=True)
    q3 = models.IntegerField(blank=True, null=True)
    q4 = models.IntegerField(blank=True, null=True)
    q5 = models.IntegerField(blank=True, null=True)
    q6 = models.IntegerField(blank=True, null=True)
    q7 = models.IntegerField(blank=True, null=True)
    q8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_csn209'


class Student(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    sid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    branch = models.CharField(max_length=3, blank=True, null=True)
    email_id = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    tid = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    email_id = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teacher'

class StudentEnrolled(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    sid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student_enrolled'
        unique_together = (('course_id', 'sid'),)

class Courses(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=30, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'

class TeacherTeaches(models.Model):
    tid = models.IntegerField(primary_key=True)
    course_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'teacher_teaches'
        unique_together = (('tid', 'course_id'),)