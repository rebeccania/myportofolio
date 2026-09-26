import uuid
from django.contrib.auth.models import User 
from django.db import models

# Create your models here.
class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Education(models.Model):
    THEME_CHOICES = [
        ("amber", "Amber"),
        ("cyan", "Cyan"),
        ("purple", "Purple"),
        ("rose", "Rose"),
    ]

    level_type = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.CharField(max_length=20)
    description = models.TextField()
    tags = models.CharField(max_length=300, blank=True)
    color_theme = models.CharField(max_length=10, choices=THEME_CHOICES, default="amber")

    def __str__(self):
        return f"{self.title} - {self.institution}"
    def get_tags_list(self):
        """Memecah string tags berdasarkan koma dan merapikannya"""
        if not self.tags:
            return []
        return [tag.strip() for tag in self.tags.split(",")]

class AboutTrait(models.Model):
    emoji = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(User, related_name="starred_projects", blank=True)

    def __str__(self):
        return self.title