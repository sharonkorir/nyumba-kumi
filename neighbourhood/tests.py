from django.test import TestCase
from .models import Neighbourhood

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
  def setUp(self):
        self.new_neighbourhood = Neighbourhood(id= 1, name='west', location='langata', health_dept= '911', police_dept= '911', logo= 'random.jpg')

  def test_instance(self):
      self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))

  def tearDown(self):
     Neighbourhood.objects.filter(id=1).delete()

  def test_create_neighbourhd(self):
      self.new_neighbourhood.create_neighbourhd()
      self.assertTrue(len(Neighbourhood.objects.all())>0)

  def test_delete_neighbourhd(self):
      self.new_neighbourhood.delete_neighbourhd(1)
      self.assertTrue(len(Neighbourhood.objects.all()) == 0)

  def test_find_neighbourhd(self):
      self.new_neighbourhood.create_neighbourhd()
      self.assertTrue(len(Neighbourhood.objects.filter(id=1)) == 1)

  def test_update_neighbourhd(self):
      self.new_neighbourhood.create_neighbourhd()
      pass

    