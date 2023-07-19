from django.db import models
from django.urls import reverse
from users.models import Profile

# Create your models here.


class Classroom(models.Model):
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=7)
    students = models.ManyToManyField(Profile, blank=True, related_name="classroomstudents")

    def __str__(self):
        return self.code


class Comment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    commentor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=400)
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_text
        


class Pdf(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=400) 
    pdflink = models.FileField(upload_to='pdfs/')
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

 