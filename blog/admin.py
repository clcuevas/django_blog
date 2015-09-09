from django.contrib import admin
# Import your Post model from the models.py file
from .models import Post

# Register your models here.
admin.site.register(Post)
