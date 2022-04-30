import sympy as smp
import math
from math import log

def bisection_method(function, xl, xr, error):
    """
    Approximation solution of g(x) = 0 on the interval [xl, xr] by bisection
    method algorithm.
​
    Parameters:
    -----------
    function: The function for which we are trying to approximate a solution
              of g(x) = 0
    xl, xr  : The interval in which to search for a solution. The function
              returns None if both g(xl), g(xr) < 0 or g(xl), g(xr) > 0 since
              a solution is not guaranteed.
    error   : The error accuracy of the test usually takes a value that is
              close to zero. The error is usually denoted by the epsilon
              symbol.
    Returns:
    --------
    Iteration number: The number of iteration that have taken place depending
                      how many times it takes to arrive at optimum.
    First Approximation Root (xl): The left root boundary of a particular
                                   iteration.
    Second Approximation Root (xr): The right root boundary of a particular
                                    iteration.
    |xr - xl|: The absolute difference of the two approximation root. The
               program reaches stopping criterion if the value is less than
               error epsilon.
    xm: The midpoint of the two approximation root
    g(xm): The value of g(x) when it takes in the midpoint of the two
           approximation root (xm).
    """
​
    def derivative(func):
        x = smp.symbols("x", real=True)
        output = smp.diff(eval(func), x)
        return str(output)
​
    def g(x):
        return eval(derivative(function))
​
    condition = g(xl) < 0 < g(xr)
    iteration = 1
    while condition is True:
        print(f"Iteration number: {iteration}")
        print(f"First Approximation Root (xl): {xl}")
        print(f"Second Approximation Root (xr): {xr}")
        print(f"|xr - xl| = {abs(xr - xl)}")
        if abs(xr - xl) < error:
            optimum = (xl + xr) / 2
            print(f"Optimal Solution: x = {optimum}")
            print(f"g(x*) = {g(optimum)}")
            break
        else:
            xm = (xl + xr) / 2
            print(f"xm: {xm}")
            print(f"g(xm) = {g(xm)}")
            if g(xm) == 0:
                optimum = xm
                print(f"Optimal Solution: x = {optimum}")
                print(f"g(x*) = {g(optimum)}")
                break
            else:
                if g(xm) > 0:
                    xr = xm
                elif g(xm) < 0:
                    xl = xm
​
        print(f"{'-' * 60}")
        iteration += 1
