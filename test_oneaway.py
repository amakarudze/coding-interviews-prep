"""Tests for oneaway module using unittest library and not pytest."""

import unittest

from oneaway import one_away


class OneAwayTest(unittest.TestCase):

    def test_one_edit(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))

    def test_not_one_edit(self):
        self.assertFalse(one_away('pale', 'bake'))
        self.assertFalse(one_away('eat', 'drink'))


if '__name__' == '__main__':
    unittest.main()
