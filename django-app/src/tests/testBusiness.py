from django.test import TestCase
from django.contrib.localflavor.us.models import USStateField
from api.models import Business

class BusinessTestCase(TestCase):
  def setUp(self):
    Business.objects.create(name="Test Business 1", \
      address_1="123 Test Address 1",               \
      address_2="Suite 420",                        \
      city="Portland"                               \
      state=USStateField.clean('OR')                \
      zip="97214")

  def testBusinessProperties(self):
    """Verify business fields are set"""
    test_business = Business.objects.get(name="Test Business 1")
    self.assertEqual(testBusiness.address_1, "123 Test Address 1")
    self.assertEqual(testBusiness.address_2, "Suite 420")
    self.assertEqual(testBusiness.city, "Portland")
    self.assertEqual(testBusiness.state, USStateField.clean('OR'))
    self.assertEqual(testBusiness.zip, "97214")
    