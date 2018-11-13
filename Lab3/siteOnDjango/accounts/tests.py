from django.test import TestCase
from django.contrib.auth.models import User
from mainApp.models import Events
from mainApp.models import Follow
import datetime
from django.utils import timezone



class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username = "test", first_name = "test_f", last_name = "test_l", password = "test_p")

    def testUser(self):
        user = User.objects.get(username = "test")
        self.assertEqual(user.username, "test")
        self.assertEqual(user.first_name, "test_f")
        self.assertEqual(user.last_name, "test_l")
        self.assertEqual(user.password, "test_p")


class EventTestCase(TestCase):
    def setUp(self):
        event = Events.objects.create(title = "test_t", description = "test_desc", date = datetime.datetime(2020, 11, 11, tzinfo=timezone.utc))

    def testEvent(self):
        event = Events.objects.get(title = "test_t")
        self.assertEqual(event.title, "test_t")
        self.assertEqual(event.description, "test_desc")
        self.assertEqual(event.date, datetime.datetime(2020, 11, 11, tzinfo=timezone.utc))

class FollowTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = "test", first_name = "test_f", last_name = "test_l", password = "test_p")
        self.event = Events.objects.create(title = "test_t", description = "test_desc", date = datetime.datetime(2020, 11, 11, tzinfo=timezone.utc))
        self.follow = Follow.objects.create(user_id = self.user, event_id = self.event)

    def testFollow(self):
        user = User.objects.get(username = "test")
        event = Events.objects.get(title = "test_t")
        self.assertEqual(self.follow.user_id, user)
        self.assertEqual(self.follow.event_id, event)

# class LoginTestCase(TestCase):
#     def setUp(self):
#         data = {"username": "test", "first_name": "test_f", "last_name": "test_l", "password1": "password_000", "password2": "password_000"}
#         UserForm(data).save()

    # def test_login(self):
    #     r = self.client.get("/accounts/login/?username=test&password=password_000")
    #     self.assertEqual(r.status_code, 200)

#
# class RegisterTestCase(TestCase):
#     def test_register(self):
#         r = self.client.get("accounts/signup/?username=test&first_name=test_f&last_name=test_l&password=test_p&confPassword=test_p")
#         self.assertEqual(r.status_code, 200)





if __name__ == '__main__':
    unittest.main(verbosity=2)
