from django.contrib import admin
import blog.models as models

admin.site.register(models.Post)

admin.site.register(models.Theme)

admin.site.register(models.Comment)


# Register your models here.
