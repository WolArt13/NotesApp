from django.test import TestCase

# Create your tests here.
class MyTest(TestCase):
    
    def test_one(self):
        self.assertTrue(True)
    
    def test_two(self):
        self.assertFalse(False)
        
    def test_three(self):
        self.assertEqual(1, 1)