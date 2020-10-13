#!/usr/bin/python3
"""
Test Rectangle Unitest
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
from os import path, remove
from unittest.mock import patch
import io


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

    def test_nowidth(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_noheight(self):
        """ Test for no height """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_nox(self):
        """ Test for no x """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.x, 0)

    def test_noy(self):
        """ Test for no y """
        r1 = Rectangle(1, 1, 1)
        self.assertEqual(r1.y, 0)

    def test_noid(self):
        """ Test for no id """
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.id, 1)

    def test_id(self):
        """ Test for id """
        r1 = Rectangle(1, 1, 1, 1, 85)
        self.assertEqual(r1.id, 85)

    def test_extraarg(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, 1, 1, 1)


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

    def test_y(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r2.x, 3)
        self.assertEqual(self.r3.x, 12)
        self.assertEqual(self.r4.x, 17)

    def test_x_INT_neg(self):
        """ Negative Int for x """
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, -1)

    def test_x_INT_zero(self):
        """ Zero Int for x """
        r1 = Rectangle(1, 5, 0)
        self.assertEqual(r1.x, 0)

    def test_x_float(self):
        """ pos float for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1.0)

    def test_x_None(self):
        """ None for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)

    def test_x_str(self):
        """Test non-ints for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)

    def test_x_List(self):
        """ List for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, [5])

    def test_x_Tuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2, (1, ))

    def test_x_Set(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 1, {1})

    def test_x_private(self):
        """ Check private x """
        r1 = Rectangle(1, 1, 5)
        self.assertEqual(r1.x, 5)
        with self.assertRaises(AttributeError):
            r1.__x


class Test_y(unittest.TestCase):
    """Class test_with"""

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(1, 2, 4, 7)
        self.r2 = Rectangle(1, 2, 3, 5)
        self.r3 = Rectangle(10, 11, 12, 13, 14)
        self.r4 = Rectangle(2, 16, 17, 18)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 7)
        self.assertEqual(self.r2.y, 5)
        self.assertEqual(self.r3.y, 13)
        self.assertEqual(self.r4.y, 18)

    def test_y_INT_neg(self):
        """ Negative Int for y """
        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 5, 6, -1)

    def test_y_INT_zero(self):
        """ Zero Int for y """
        r1 = Rectangle(1, 5, 1, 0)
        self.assertEqual(r1.y, 0)

    def test_y_float(self):
        """ pos float for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 4, 4.4)

    def test_y_None(self):
        """ None for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 3, None)

    def test_y_str(self):
        """Test non-ints for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 4, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 3, True)

    def test_y_List(self):
        """ List for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 5, 3, [8])

    def test_y_Tuple(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2, 4, (5, ))

    def test_y_Set(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 1, 2, {13})

    def test_y_private(self):
        """ Check private y """
        r1 = Rectangle(1, 1, 5, 9)
        self.assertEqual(r1.y, 9)
        with self.assertRaises(AttributeError):
            r1.__y


class Test_area(unittest.TestCase):
    """ Class for unittest of area method """

    def test_area1(self):
        """ Area 1 """
        r1 = Rectangle(2, 5)
        self.assertEqual(r1.area(), 10)

    def test_area2(self):
        """ Area 2 """
        r1 = Rectangle(1, 4)
        self.assertEqual(r1.area(), 4)

    def test_area3(self):
        """ Area 2 """
        r1 = Rectangle(3, 3, 1, 1, 1)
        self.assertEqual(r1.area(), 9)


class Test_display(unittest.TestCase):
    """ Class for unittest of display method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_noxy0(self):
        """ Display no XY """
        r1 = Rectangle(1, 1)
        dp = "#\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy1(self):
        """ Display no XY """
        r1 = Rectangle(2, 2)
        dp = "##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy2(self):
        """ Display no XY """
        r1 = Rectangle(3, 2)
        dp = "###\n###\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noxy3(self):
        """ Display no XY """
        r1 = Rectangle(2, 3)
        dp = "##\n##\n##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noy0(self):
        """ Display no Y """
        r1 = Rectangle(2, 3, 1)
        dp = " ##\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_noy1(self):
        """ Display no Y """
        r1 = Rectangle(2, 3, 1)
        r1.x = 3
        dp = "   ##\n   ##\n   ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_xydisplay0(self):
        """ Display XY """
        r1 = Rectangle(2, 3, 1, 2)
        dp = "\n\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)

    def test_xydisplay1(self):
        """ Display XY """
        r1 = Rectangle(2, 3, 1, 2)
        r1.x = 2
        r1.y = 3
        dp = "\n\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=io.StringIO()) as p:
            r1.display()
            st = p.getvalue()
        self.assertEqual(st, dp)


class Test_str(unittest.TestCase):
    """ Class for unittest of __str__ method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_str1(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3)
        st = "[Rectangle] (1) 0/0 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str2(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5)
        st = "[Rectangle] (1) 5/0 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str3(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6)
        st = "[Rectangle] (1) 5/6 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str4(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6, 85)
        st = "[Rectangle] (85) 5/6 - 2/3"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)

    def test_str5(self):
        """ Test for __str__ """
        r1 = Rectangle(2, 3, 5, 6, 85)
        r1.id = 9
        r1.x = 8
        r1.y = 7
        r1.width = 6
        r1.height = 5
        st = "[Rectangle] (9) 8/7 - 6/5"
        strP = str(r1)
        self.assertEqual(st, strP)
        with patch('sys.stdout', new=io.StringIO()) as p:
            print(r1, end='')
            pr = p.getvalue()
        self.assertEqual(st, pr)
