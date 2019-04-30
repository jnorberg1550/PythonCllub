from django.db import models


class MeetingType(models.Model):
    meetingtitle=models.Charfield (max_length='64')
    meetingdate=models.Datefield()
    meetingtime=models=models
    meetinglocation==models.Charfield (max_length='256')
    meetingagenda=models.Charfield (max_length='256')
 

 class MeetingMinutes(models.Model):
    minutesid=models.ForeignKey (MeetingType, on_delete models.DO_NOTHING)
    minutesattendance=models.ManyToManyField(User)
    minutestext=models.TextField()

class MeetingResource
    resourcename=models.Charfield (max_length='64')
    resourcetype=models.Charfield (max_length='64')
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.Datefield()
    resourceuserid
    resourcedescription=models.TextField()

class MeetingEvent
    eventtitle=models.Charfield (max_length='64')
    eventlocation=models.Charfield (max_length='64')
    eventdate=models.Datefield()
    eventtime
    eventdescription=models.TextField()
    eventuserid