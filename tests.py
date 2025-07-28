from unittest import TestCase

from pylib25 import sqr


class Test(TestCase):
    def test_sqr(self):
        self.assertEqual(sqr(5.0), 25.0)
