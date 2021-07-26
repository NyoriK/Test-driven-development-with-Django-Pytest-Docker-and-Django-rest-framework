from .. import models
from .. import admin
from django.contrib.admin.sites import AdminSite
import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestTaskAdmin:
    def test_excerpt(self):
        site = AdminSite()
        task_admin = admin.TaskAdmin(models.Task, site)

        obj = mixer.blend('tasks.Task', title='Buy milk from the market')
        result = task_admin.excerpt(obj)
        assert result == 'Buy milk', 'Should return first few characters'
