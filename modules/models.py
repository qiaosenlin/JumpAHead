from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=500, null=False,primary_key=True)
    description = models.TextField(blank=True)


class Module(models.Model):
    video_link = models.URLField(max_length=250, blank=True)
    title = models.CharField(max_length=500, primary_key=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    description = models.TextField()
    delivery_strategy = models.TextField()
    grouping_used = models.TextField()
    skills = models.TextField()
    materials = models.TextField()
    course = models.ForeignKey(Course,to_field="title",
                               on_delete=models.CASCADE,
                               related_name="modules")



class Task(models.Model):
    module = models.ForeignKey(Module,to_field="title",
                               on_delete=models.CASCADE,
                               related_name="tasks")
    description = models.TextField()
    checkComplete = models.BooleanField(default = False, verbose_name = "")
    taskNum = models.IntegerField()
