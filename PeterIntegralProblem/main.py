import numpy as np
from math import *

# f_str = input("f(x) = ")
# a = int(input("a = "))
# b = int(input("b = "))
# deg = int(input("deg( p(x) ) = "))
# N = input("N = ")

f_str = "cos(x)"
a = -2
b = 2
deg = 2
N = 100000


f = lambda x: eval(f_str)
mu = lambda i: (a*i+b*i)/N

def S( g ):
    sum = 0
    for i in range(1, N+1):
        sum += g(i)
    
    return sum

A = np.array([
    [
        S( lambda i:mu(i)**(deg*2-x-y) ) for y in range(deg+1)
    ] for x in range(deg+1)
])

b = np.array([
    S( lambda i:f(mu(i))*mu(i)**j ) for j in range(deg, -1, -1)
])

solution = np.linalg.solve(A, b)
print("Coefficients are ", np.round(solution, decimals=3))