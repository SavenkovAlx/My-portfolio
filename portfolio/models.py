from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=33)
    image = models.ImageField(upload_to='portfolio/images')
    project_url = models.URLField(blank=True)
    github_url = models.URLField()
