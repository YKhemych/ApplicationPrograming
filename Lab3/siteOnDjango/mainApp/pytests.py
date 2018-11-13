from django.contrib.auth.models import User
from mainApp.models import Events
from mainApp.models import Follow
import datetime
from django.utils import timezone
import pytest

@pytest.mark.django_db
def testUser(self):
    user = User.objects.create(username = "test", first_name = "test_f", last_name = "test_l", password = "test_p")
    assert user.username == "test"
    assert user.first_name == "test_f"
    assert user.last_name == "test_l"
    assert user.password == "test_p"



@pytest.mark.django_db
def testEvent(self):
    event = Events.objects.create(title = "test_t", description = "test_desc", date = datetime.datetime(2020, 11, 11, tzinfo=timezone.utc))
    assert event.title == "test_t"
    assert event.description == "test_desc"
    assert event.date == datetime.datetime(2020, 11, 11, tzinfo=timezone.utc)

@pytest.mark.django_db
def testFollow(self):
    self.user = User.objects.create(username = "test", first_name = "test_f", last_name = "test_l", password = "test_p")
    self.event = Events.objects.create(title = "test_t", description = "test_desc", date = datetime.datetime(2020, 11, 11, tzinfo=timezone.utc))
    self.follow = Follow.objects.create(user_id = self.user, event_id = self.event)
    assert self.follow.user_id == user
    assert self.follow.event_id == event)
