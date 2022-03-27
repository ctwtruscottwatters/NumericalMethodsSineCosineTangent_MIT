# -*- coding: utf-8 -*-
import math
import sys
import numpy

"""
I LOVE MIT

INFINITE SERIES FOR THE SINE, COSINE, AND TANGENT

CHARLES THOMAS WALLACE TRUSCOTT

BYRON BAY NSW 2481

"""

def ramanujans_pi():
    
    """
    This numerical method is authored by Charles Truscott after sitting a unit at MIT in Computation and Programming using Python
    I love MIT. Proud to hold my certificate by the end of this year. Always showing off as an MIT certificate holder
    Thanks National Security Agency
    Byron Bay NSW 2481
    """
    x = 2 * numpy.sqrt(2)
    y = 9801
    pi = 0
    summation = 0
    for k in range(0, 5, 1):
        numerator = ((math.factorial(4 * k)) * ((1103 + (26390 * k))))
        denominator = ((math.factorial(k) ** 4) * ((396 ** (4 * k))))
        summation += numerator / denominator
    pi = (x / y) * summation
    pi = 1.0 / pi
    print('The reciprocal of the summation after multiplying by the coefficient is: {} (Pi)'.format(pi))
    # Authored by Charles Thomas Wallace Truscott Watters
    return pi

def sine_taylor(find_answer, pi_value):
    odd_numbers = []
    for n in range(0, 100):
        if n % 2 == 0:
            continue
        else:
                odd_numbers.append(n)
    print('You input {} to find the sine for ... \n using Ramanujan\'s approximation for Pi at {}'.format(find_answer, pi_value))
    dummy_val = float(find_answer) * pi_value / 180
    num = dummy_val
    index = 0
    for n in odd_numbers:
        print('approximation of sine is currently: {} -/+{}!? {}'.format(num, n, 'Subtract x ^ n / n!' if index % 2 == 0 else 'Add x ^ n / n!'))
        if index % 2 == 0:
                num -= ((dummy_val ** n))/((math.factorial(n)))
        else:
                num += ((dummy_val ** n))/((math.factorial(n)))
        index += 1
    print(pi)
    print('Subtracting x: {}'.format(num))
    num = dummy_val - num
    print('{}'.format(num))
    print('Sine of {} is {}'.format(find_answer, num))
    # Authored by Charles Thomas Wallace Truscott Watters
    return num


def cosine_taylor(find_answer, pi_value):
    if find_answer == 90.0:
        return 0
    elif find_answer == 0.0:
        return 1
    even_numbers = []
    for n in range(0, 100):
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            continue
    print('You input {} to find the cosine for ... \n using Ramanujan\'s approximation for Pi at {}'.format(find_answer, pi_value))
    dummy_val = float(find_answer) * pi_value / 180
    num = 1
    index = 0
    for n in even_numbers:
      print('approximation of cosine is currently: {} -/+{}!? {}'.format(num, n, 'Add x ^ n / n!' if index % 2 == 0 else 'Subtract n ^ x / n!'))
      if index % 2 == 0:
          num += ((dummy_val ** n))/((math.factorial(n)))
      else:
          num -= ((dummy_val ** n))/((math.factorial(n)))
      index += 1
    print('Subtracting 1 from {}'.format(num))
    num = 1 - num
    print('{}')
    print('Cosine of {} is {}'.format(find_answer, num))
    return abs(num)
    
def find_tangent(sine_value, cosine_value):
    if sine_value == 0 or cosine_value == 0:
        return 0
    else:
        return sine_value / cosine_value

pi = ramanujans_pi()
print('Authored by {} {} {} {} {} after sitting a unit at MIT'.format('Charles', 'Thomas', 'Wallace', 'Truscott', 'Watters'))
degree_value = float(input('Enter a value in degrees to calculate the sine, cosine and tangent for :-) :\t'))
sine = sine_taylor(degree_value, pi)

cosine = cosine_taylor(degree_value, pi)
tangent = find_tangent(sine, cosine)

print('The sine of {} is {}; the cosine of {} is {}; the tangent of {} is {}; Ramanujan\'s Infinite Series for Pi approximates to: {}'.format(degree_value, sine, degree_value, cosine, degree_value, tangent, pi))