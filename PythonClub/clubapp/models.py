from django.db import models

from django.contrib.auth.models import User



class MeetingType(models.Model):
    meetingtitle=models.Charfield (max_length='64')
    meetingdate=models.Datefield()
    meetingtime=models=models.Integer(max_length = '4')
    meetinglocation==models.Charfield (max_length='256')
    meetingagenda=models.Textfield()

class Meta:
    db_table='meetings'
    verbose_name_plural='MeetingTypes
 
 

 class MeetingMinutes(models.Model):
    minutesid=models.ForeignKey (MeetingType, on_delete models.DO_NOTHING)
    minutesattendance=models.ManyToManyField(User)

class Meta:
    db_table= 'minutes'
    verbose_name_plural='MeetingMinutes'


    def __str__(self):
        return self.typename
    


class MeetingResource
    resourcename=models.Charfield (max_length='64')
    resourcetype=models.Charfield (max_length='64')
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.Datefield()
    resourceuserid=models.Integer(max_length = '7')
    resourcedescription=models.TextField()

    class Meta:
    db_table= 'resource'
    verbose_name_plural='MeetingResources'

    def __str__(self):
        return self.typename
    

class MeetingEvent
    eventtitle=models.Charfield (max_length='64')
    eventlocation=models.Charfield (max_length='64')
    eventdate=models.Datefield()
    eventtime=models.Integer(max_length = '4')
    eventdescription=models.TextField()
    eventuserid=models.ManyToManyField(User)

   class Meta:
        db_table= 'events'
        verbose_name_plural='MeetingEvents' 

def __str__(self):
        return self.typename



# Register your models here.







