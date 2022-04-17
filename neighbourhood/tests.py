from django.test import TestCase
from .models import Neighbourhood

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
  def setUp(self):
        self.new_neighbourhood = Neighbourhood(name='west', location='langata', health_dept= 'langata hosp', police_dept= 'langata police station', logo= 'random.jpg')

  def test_instance(self):
      self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))

  def tearDown(self):
     Neighbourhood.objects.filter(id=1).delete()

  def test_create_neighbourhd(self):
      self.new_neighbourhood.create_neighbourhd()
      self.assertTrue(len(Neighbourhood.objects.all())>0)

  def test_delete_neighbourhd(self):
    self.new_neighbourhood.delete_neighbourhd('west')
    self.assertTrue(len(Neighbourhood.objects.all()) == 0)

  def test_find_neighbourhd(self):
    self.new_neighbourhood.create_neighbourhd()
    self.assertTrue(len(Neighbourhood.objects.filter(id=1)) == 0)

    