from django.contrib import admin

# Register your models here.
# username= laptop
#pass=laptop123

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
