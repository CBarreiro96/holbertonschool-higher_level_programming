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


class Test_width(unittest.TestCase):
    """Class test_with"""

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(11, 11)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(10, 11, 12, 13, 14)
        self.r4 = Rectangle(2, 16, 17, 18)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 11)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r4.width, 2)

    def test_width_INT_neg(self):
        """ Negative Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-7, 5)

    def test_width_INT_zero(self):
        """ Zero Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 5)

    def test_width_float(self):
        """ pos float for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1.0, 1)

    def test_width_str(self):
        """Test non-ints for width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)

    def test_width_List(self):
        """ List for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle([5], 5)

    def test_width_Tuple(self):
        """ Tuple for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle((3, ), 2)

    def test_width_Set(self):
        """ Set for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle({4}, 1)


    def test_width_private(self):
        """ Check private Width """
        r1 = Rectangle(13, 7)
        self.assertEqual(r1.width, 13)
        with self.assertRaises(AttributeError):
            r1.__width


class Test_height(unittest.TestCase):
    """Class test height"""


    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(11, 11)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(10, 11, 12, 13, 14)
        self.r4 = Rectangle(2, 16, 17, 18)


    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 11)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r3.height, 11)
        self.assertEqual(self.r4.height, 16)

    def test_height_str(self):
        """Test non-ints for height"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)

    def test_heightintneg(self):
        """ Negative Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -5)


    def test_height_INT_zero(self):
        """ Zero Int for height """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)

    def test_height_float(self):
        """ pos float for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.0)

    def test_height_List(self):
        """ List for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, [5])

    def test_height_Tuple(self):
        """ Tuple for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle((3, ), 2)

    def test_height_Set(self):
        """ Set for height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, {1})


    def test_height_private(self):
        """ Check private height """
        r1 = Rectangle(13, 7)
        self.assertEqual(r1.height, 7)
        with self.assertRaises(AttributeError):
            r1.__height

class Test_x(unittest.TestCase):
    """Class test_with"""

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(1, 2, 4)
        self.r2 = Rectangle(1, 2, 3)
        self.r3 = Rectangle(10, 11, 12, 13, 14)
        self.r4 = Rectangle(2, 16, 17, 18)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.x, 12)
        self.assertEqual(self.r4.x, 17)

    def test_width_x_INT_neg(self):
        """ Negative Int for Width """
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, -1)

    def test_width_x_INT_zero(self):
        """ Zero Int for Width """
        r1 = Rectangle(1, 5, 0)
        self.assertEqual(r1.x, 0)

    def test_width_x_float(self):
        """ pos float for Width """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1.0)

    def test_x_None(self):
        """ None for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)

    def test_width_x_str(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_width_x_List(self):
        """ List for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, [5])

    def test_width_x_Tuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2, (1, ))

    def test_width_x_Set(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 1, {1})


    def test_xprivate(self):
        """ Check private x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)
        with self.assertRaises(AttributeError):
            r1.__x
