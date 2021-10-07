# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertNotEqual(classify_triangle(3,3,6), 'Right', '3 3 6 is not a right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(classify_triangle(1,1,2), 'Equilateral', '1 1 2 is not an equilateral triangle')

    def testInvalidInput(self):
        self.assertEqual(classify_triangle(201, 1, 1), 'InvalidInput', '201 1 1 is not valid input')
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidInput', '-1 1 1 is not valid input')
        self.assertEqual(classify_triangle(1, -1, 1), 'InvalidInput', '1 -1 1 is not valid input')
        self.assertEqual(classify_triangle(1.2, 1.3, 1.5), 'InvalidInput', '1.2 1.3 1.5 is not a valid input')
        self.assertEqual(classify_triangle(1.2, 1, 1), 'InvalidInput', '1.2 1 1 is not valid input')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(100, 5, 2), 'NotATriangle', '100 5 2 is not a valid triangle')
        self.assertEqual(classify_triangle(5, 100, 2), 'NotATriangle', '5 100 2 is not a valid triangle')
        self.assertEqual(classify_triangle(2, 5, 100), 'NotATriangle', '2 5 100 is not a valid triangle')

    def testScalene(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '2 4 6 is a scalene triangle')
        self.assertNotEqual(classify_triangle(5, 2, 5), 'Scalene', '5 2 5 is not a scalene triangle')

    def testIsosceles(self):
        self.assertEqual(classify_triangle(5, 2, 5), 'Isoceles', '5 2 5 is a isoceles triangle')
        self.assertEqual(classify_triangle(5, 5, 8), 'Isoceles', '5 5 21 is a isosceles triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

