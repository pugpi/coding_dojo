import unittest

from pugpi import feliz 
class PugPITestCase(unittest.TestCase):

	def test_7(self):
		self.assertTrue(feliz(7))

	def test_49(self):
		self.assertTrue(feliz(49))

	def test_3(self):
		self.assertFalse(feliz(3))

	def test_6(self):
		self.assertFalse(feliz(6))