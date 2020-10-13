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

def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r3.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 8 +
                             (" " * 7 + "#" * 5 + "\n") * 6)

        with io.StringIO() as buf, redirect_stdout(buf):
            self.r4.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 14 +
                             (" " * 13 + "#" * 11 + "\n") * 12)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="hello")
        with self.assertRaises(TypeError):
            r.update(height="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_extra_kwargs(self):
        """tests for random kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dict(self):
        """test regular to_dictionary"""
        d1 = self.r1.to_dictionary()
        self.assertEqual({"id": 1, "width": 10, "height": 10, "x": 0, "y": 0},
                         d1)
        d2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 2, "height": 3, "x": 4, "y": 0},
                         d2)
        d3 = self.r3.to_dictionary()
        self.assertEqual({"id": 9, "width": 5, "height": 6, "x": 7, "y": 8},
                         d3)
        d4 = self.r4.to_dictionary()
        self.assertEqual({"id": 3, "width": 11, "height": 12, "x": 13,
                          "y": 14}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**d4)
        self.assertEqual(str(r), str(self.r4))
        self.assertNotEqual(r, self.r4)

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """test save_to_file with empty list"""
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_None(self):
        """test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        r1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r2 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_load_from_file_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Checks use of load_from_file with empty file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """test normal use of load_from_file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1c = lo[0]
        r2c = lo[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)
