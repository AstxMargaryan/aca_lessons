from django.contrib import admin
from .models import Question, Choice, PollUser, ApiKey
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollUser)
admin.site.register(ApiKey)
