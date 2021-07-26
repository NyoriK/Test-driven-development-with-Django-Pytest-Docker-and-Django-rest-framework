import pytest
from mixer.backend.django import mixer


@pytest.mark.django_db
class TestTask:
    def test_model(self):
        obj = mixer.blend('tasks.Task')
        assert obj.pk == 1, 'Should create a task instance'

    def test_excerpt(self):
        obj = mixer.blend('tasks.Task', title='Buy milk from the market')
        result = obj.get_excerpt(8)
        assert result == 'Buy milk', 'Should return first few characters'
