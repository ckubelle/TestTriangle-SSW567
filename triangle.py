# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def r_t_c(f_s,s_s,t_s):
    """Method checks if right triangle"""
    if f_s*f_s + s_s*s_s == t_s*t_s:
        return True
    return False


def check_invalid_input(a_s, b_s, c_s):
    """Checks if input is invalid"""
    if a_s > 200 or b_s > 200 or c_s > 200:
        return True
    if a_s <= 0 or b_s <= 0 or c_s <= 0:
        return True
    if not(isinstance(a_s,int) and isinstance(b_s,int) and isinstance(c_s,int)):
        return True
    return False

def classify_triangle(a_s,b_s,c_s):
    """
    Your correct code goes here... Fix the faulty logic below until the code passes all of
    you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if check_invalid_input(a_s,b_s,c_s):
        return 'InvalidInput'
    if (a_s >= (b_s + c_s)) or (b_s >= (a_s + c_s)) or (c_s >= (a_s + b_s)):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a_s == b_s and b_s == c_s:
        return 'Equilateral'
    if r_t_c(a_s,b_s,c_s) or r_t_c(a_s,c_s,b_s) or r_t_c(c_s,b_s,a_s):
        return 'Right'
    if (a_s != b_s) and  (b_s != c_s) and (a_s != c_s):
        return 'Scalene'
    return 'Isoceles'
