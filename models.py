from django.db import models


from django.contrib.auth.models import User



class MeetingType(models.Model):
    meetingtitle=models.Charfield (max_length='64')
    meetingdate=models.Datefield()
    meetingtime=models=models.Integer (max_length='4')
    meetinglocation==models.Charfield (max_length='255')
    meetingagenda=models.Charfield (max_length='255')
 
    class Meta:
        db_table='meetings'
        verbose_name_plural='MeetingTypes'

    def __str__(self):
        return self.meetingtitle

 class MeetingMinutes(models.Model):
    minutesid=models.ForeignKey (MeetingType, on_delete models.DO_NOTHING)
    minutesattendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    class Meta:
        db_table= 'minutes'
        verbose_name_plural='MeetingMinutes'

    def __str__(self):
        return self.minutesid


class MeetingResource
    resourcename=models.Charfield (max_length='64')
    resourcetype=models.Charfield (max_length='64')
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.Datefield()
    resourceuseridmodels.Charfield (User)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
    db_table= 'resource'
    verbose_name_plural='MeetingResources'
   

class MeetingEvent
    eventtitle=models.Charfield (max_length='64')
    eventlocation=models.Charfield (max_length='64')
    eventdate=models.Datefield()
    eventtime=models.
    eventdescription=models.TextField()
    eventuserid=models.Charfield (User)

    
    class Meta:
        db_table= 'events'
        verbose_name_plural='MeetingEvents'


    def __str__(self):
        return self.eventtitle

# Register your models here.

