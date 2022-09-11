from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class SiteSettings(models.Model):
    about = RichTextField(verbose_name="Bioqrafiya")
    instagram = models.CharField(max_length=100,verbose_name="Instagram")
    facebook = models.CharField(max_length=100,verbose_name="Facebook")
    youtube = models.CharField(max_length=100,verbose_name="Youtube")
    linkedin = models.CharField(max_length=100,verbose_name="Linkedin")

    def __str__(self):
        return "Sayt Tənzimləmələri"