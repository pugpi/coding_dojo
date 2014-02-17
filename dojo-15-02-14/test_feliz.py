import unittest

from feliz import feliz


class NumeroFelizTestCase(unittest.TestCase):

    def test_7_is_happy(self):
        self.assertTrue(feliz(7))

    def test_49_is_happy(self):
        self.assertTrue(feliz(49))

    def test_3_is_unhappy(self):
        self.assertFalse(feliz(3))

    def test_6_is_unhappy(self):
        self.assertFalse(feliz(6))