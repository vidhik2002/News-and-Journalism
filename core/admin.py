from django.contrib import admin
from .models import(
    Article,Reporter,Subord

)
admin.site.register(
    Article
)
admin.site.register(
    Reporter
)
admin.site.register(
    Subord
)
# Register your models here.
