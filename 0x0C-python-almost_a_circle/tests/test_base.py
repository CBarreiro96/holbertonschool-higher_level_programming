#!/usr/bin/env python
"""Tests Base Unitest"""

import unittest
from models.base import Base
import json
from models.rectangle import Rectangle
from models.square import Square


class Test_id(unittest.TestCase):
    """Class test id"""
    def test_no_arg(self):
        """ Id no argument """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_none(self):
        """ Id None """
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)
        b3 = Base(None)
        self.assertEqual(b3.id, 3)

    def test_id_set(self):
        """Tests id as not None"""
        b100 = Base(100)
        self.assertEqual(b100.id, 100)

    def test_nb_private(self):
        """Tests nb_objects as a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_extra_args(self):
        """ More than 1 argument """
        with self.assertRaises(TypeError):
            b1 = Base(5, 1)


class Test_Json(unittest.TestCase):
    """Test case Json"""
    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_to_json_string(self):
        """Tests regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 1, "width": 3, "height": 9, "x": 4, "y": 9}
        d2 = {"id": 6, "width": 2, "height": 3, "x": 5, "y": 7}
        json_string = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_string) is str)
        d = json.loads(json_string)
        self.assertEqual(d, [d1, d2])

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 5, "width": 12, "height": 14, "x": 4, "y": 10}, \
{"id": 7, "width": 1, "height": 18, "x": 3, "y": 7}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 5, "width": 12, "height": 14, "x": 4, "y": 10})
        self.assertEqual(json_l[1],
                         {"id": 7, "width": 1, "height": 18, "x": 3, "y": 7})

    def test_Rectangle(self):
        """ Test with Rectangle instance """
        r1 = Rectangle(10, 7, 2, 8)
        l1 = [r1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        st = str(l1)
        self.assertEqual(j1, st.replace("'", "\""))

    def test_Square(self):
        """ Test with Square instance """
        s1 = Square(10, 2, 8)
        l1 = [s1.to_dictionary()]
        j1 = Base.to_json_string(l1)
        st = str(l1)
        self.assertEqual(j1, st.replace("'", "\""))


class Test_instance(unittest.TestCase):
    """ Class Test instance """
    def test_base_self(self):
        """ Check if is instance """
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))

    def test_Rectangle(self):
        """ Check if is instance """
        r1 = Rectangle(1, 1)
        self.assertTrue(isinstance(r1, Base))

    def test_Square(self):
        """ Check if is instance """
        s1 = Square(1)
        self.assertTrue(isinstance(s1, Base))


class Test_create(unittest.TestCase):
    """ Class for unittest of create method """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_Rectangle1(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle2(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle3(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8, 6)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Rectangle4(self):
        """ Test with different Rectangle instances """
        r1 = Rectangle(3, 5, 8, 6, 85)
        d1 = r1.to_dictionary()
        r2 = Rectangle.create(**d1)
        st1 = str(r1)
        st2 = str(r2)
        self.assertEqual(st1, st2)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_Square1(self):
        """ Test with different Square instances """
        s1 = Square(3)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square2(self):
        """ Test with different Square instances """
        s1 = Square(3, 4)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square3(self):
        """ Test with different Square instances """
        s1 = Square(3, 4, 5)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_Square4(self):
        """ Test with different Square instances """
        s1 = Square(3, 4, 5, 82)
        d1 = s1.to_dictionary()
        s2 = Square.create(**d1)
        st1 = str(s1)
        st2 = str(s2)
        self.assertEqual(st1, st2)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_nokwarg(self):
        """ Test with no kwarg """
        s1 = Square(3, 4, 5, 82)
        d1 = s1.to_dictionary()
        with self.assertRaises(TypeError):
            s2 = Square.create(d1)
