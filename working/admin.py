from django.contrib import admin
from .models import *

admin.site.register(Workspace)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Topic)
admin.site.register(Entry)