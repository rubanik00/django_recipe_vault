"""
Simple test for the app
"""
from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = calc.add(3, 8)
        self.assertEqual(res, 11)