from django.contrib import admin

# Register your models here.
from .models import SiteSettings

admin.site.register(SiteSettings)