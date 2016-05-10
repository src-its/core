from django.db import models

# Some classes to test creation
class Issue(models.Model):
    def __str__(self):
        return self.issue_summary 
    
    issue_summary = models.CharField(max_length=100)
    issue_elaboration = models.CharField(max_length=300)
    issue_opened = models.DateTimeField('date opened')
    issue_closed = models.BooleanField()

class Instructions(models.Model):
    title = models.CharField(max_length=50)
    step = models.CharField(max_length=100)
