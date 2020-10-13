#!/usr/bin/python3
"""
Test Rectangle Unitest
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class Test_args(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")


class Test_area(unittest.TestCase):
    """ Class Area """
    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 10)
        self.r2 = Rectangle(2, 3, 4)
        self.r3 = Rectangle(5, 6, 7, 8, 9)
        self.r4 = Rectangle(11, 12, 13, 14)

    def test_area(self):
        """test area"""
        r1 = Rectangle(13, 15)
        self.assertEqual(r1.area(), 195)
        r2 = Rectangle(30, 30)
        self.assertEqual(r2.area(), 900)
        r3 = Rectangle(7, 8)
        self.assertEqual(r3.area(), 56)
        r4 = Rectangle(24, 39)
        self.assertEqual(r4.area(), 936)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r1.area(1)
