from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

'''
By default, Django's get_user_model() function fetches the currently active user model, which defaults to
django.contrib.auth.models.User if a custom user model is not specified. However, if you've created and 
set up a custom user model in your project (through AUTH_USER_MODEL in your settings), get_user_model() will refer to your custom user model instead of the default one.
'''

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", 
            email="testuser@ryan.com", 
            password="pass1234",
            age=30,
            #car_type="gas",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@ryan.com")
        self.assertEqual(user.age, 30)
        #self.assertEqual(user.car_type, "gas")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
            age=30,
            #car_type="electric",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertEqual(admin_user.age, 30)
        # self.assertEqual(admin_user.car_type, "electric")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)