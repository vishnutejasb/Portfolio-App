from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    image = models.FileField(upload_to="project_images/", blank=True)
    completed_date=models.DateField()

    def __str__(self):
        return f"{self.title}"

# Create your models here.
