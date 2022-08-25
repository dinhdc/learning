from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):
  
  def test_create_user(self):
    email = "abc@example.com"
    password = "password"
    fullname = "abc xyz"
    user = get_user_model().objects.create(email=email, password=password, fullname=fullname)
    self.assertEqual(user.email, email)
    self.assertEqual(user.fullname, fullname)
    self.assertTrue(user.is_active)
  
  def test_create_super_user(self):
    email = "abc@example.com"
    password = "password"
    fullname = "abc xyz"
    user = get_user_model().objects.create_superuser(email=email, password=password, fullname=fullname)
    self.assertEqual(user.email, email)
    self.assertEqual(user.fullname, fullname)
    self.assertTrue(user.is_active)
    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)
  
  def test_unnomal_email_user(self):
    emails = [["abc@GMAIL.com", "abc@gmail.com"], ["ABCxyz@gmail.com", "abcxyz@gmail.com"], ["AbcXYZv2@gmail.com", "abcxyzv2@gmail.com"]]
    password = "password"
    fullname = "abc xyz"
    for email, expected in emails:
      user = get_user_model().objects.create(email=email, password=password, fullname=fullname)
      # self.assertEqual(user.email, expected)
      self.assertEqual(user.fullname, fullname)
