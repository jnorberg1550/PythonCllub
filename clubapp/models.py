from django.db import models

from django.contrib.auth.models import User

class Meta:
        db_table='meetings'
        verbose_name_plural='MeetingTypes'

class MeetingType(models.Model):
    meetingtitle=models.Charfield (max_length='64')
    meetingdate=models.Datefield()
    meetingtime=models=models
    meetinglocation==models.Charfield (max_length='256')
    meetingagenda=models.Charfield (max_length='256')
 
 class Meta:
        db_table= 'minutes'
        verbose_name_plural='MeetingMinutes'

 class MeetingMinutes(models.Model):
    minutesid=models.ForeignKey (MeetingType, on_delete models.DO_NOTHING)
    minutesattendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.typename
    
class Meta:
    db_table= 'resource'
    verbose_name_plural='MeetingResources'

class MeetingResource
    resourcename=models.Charfield (max_length='64')
    resourcetype=models.Charfield (max_length='64')
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.Datefield()
    resourceuserid
    resourcedescription=models.TextField()

    def __str__(self):
        return self.typename
    
   class Meta:
        db_table= 'events'
        verbose_name_plural='MeetingEvents'

class MeetingEvent
    eventtitle=models.Charfield (max_length='64')
    eventlocation=models.Charfield (max_length='64')
    eventdate=models.Datefield()
    eventtime=models.
    eventdescription=models.TextField()
    eventuserid=models.

    





# Register your models here.







