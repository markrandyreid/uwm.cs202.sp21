# -*- coding: utf-8 -*-
"""pa1.uwm.compsci202.sp21.rr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TCa69aXn4oWo_Z1OR17dbJ9Z8bBd07zV
"""

import numpy

def convert1():
  F_degrees = eval(input("Please enter the temperture in Fahrenheit?"))
  C_degrees = (F_degrees-32)*(5/9)
  print("Your input of", F_degrees, " Degrees Fahrenhiet converts to ", C_degrees, " Degrees Celsius")

convert1()

