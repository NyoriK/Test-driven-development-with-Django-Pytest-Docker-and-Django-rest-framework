from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    model = models.Task
    list_display = ('excerpt',)

    def excerpt(self, obj):
        return obj.get_excerpt(8)


admin.site.register(models.Task, TaskAdmin)
