from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    stud_name = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=200)
    stud_city = models.CharField(max_length=50)
    stud_zip = models.CharField(max_length=10)
    stud_email = models.CharField(max_length=50)
    stud_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.stud_name)

class Tutor(models.Model):
    tutor_id = models.IntegerField(primary_key=True, default=0)
    tutor_name = models.CharField(max_length=100)
    tutor_address = models.CharField(max_length=200)
    tutor_city = models.CharField(max_length=50)
    tutor_zip = models.CharField(max_length=10)
    tutor_email = models.CharField(max_length=50)
    tutor_phone = models.CharField(max_length=50)
    tutor_sub_expertise = models.CharField(max_length=50)
    tutor_bank = models.CharField(max_length=100)
    tutor_rt_num = models.CharField(max_length=10)
    tutor_acct_num = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.tutor_name)

class Course(models.Model):
    course_id = models.IntegerField(primary_key=True, default=0)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(blank=True)
    course_subject = models.CharField(max_length=50)
    #slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.course_name)

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, default=0)
    room_number = models.CharField(max_length=100)
    room_capacity = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.room_number)

class Schedule(models.Model):
    schedule_id = models.IntegerField()
    schedule_course_name = models.ForeignKey(Course, related_name='contents', on_delete=models.CASCADE)
    schedule_room_number = models.ForeignKey(Room, related_name='contents', on_delete=models.CASCADE)
    schedule_tutor_name = models.ForeignKey(Tutor, related_name='contents', on_delete=models.CASCADE)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()
    schedule_notes = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='schedules/%Y/%m/%d',
                              blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('schedule_course_name',)
        index_together = (('schedule_id', 'slug'),)

    def get_absolute_url(self):
        return reverse('sis:schedule_detail',
                       args=[self.schedule_id, self.slug])


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.schedule_id)