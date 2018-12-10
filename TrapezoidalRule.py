#necessery imports
#numpy for a examples functions
#pandas for a DataFrame

import numpy as np
import pandas as pd

#Simple class for Trapezoidal rule numerical tests
#Author Dawid Majchrowski WMS
#Date 19.11.2018
class QuadratureTest:
    def __init__(self, f, df, F, a, b):
        """ Constructor params:
        @f - given function
        @df - f derivative computed analytically
        @F - f integral computed analytically
        @a - lower bound
        @b - upper bound
        integral - actual Integral value of f
        cT - constant factor for fixing Q method
        """
        self.f = f
        self.df = df
        self.F = F
        self.a = a
        self.b = b
        self.integral = F(b) - F(a)
        self.cT = (b-a)*(b-a)*(df(a) - df(b))/12
    def Q(self,n):
        """computing Quadrature using Trapezoidal rule"""
        delta = (self.b-self.a)/n # length of given subinterval
        tmpSum = sum([self.f(x) for x in [self.a + i*delta for i in range(1,n)]]) # sum of f(x1),f(x2),...,f(xn-1)
        tmpSum = tmpSum + self.f(self.a)/2 + self.f(self.b)/2 # adding f(x0)/2 = f(a)/2 and  f(xn) = f(b)/2 to sum
        result = delta*tmpSum # finally multiplying current sum by delta
        return result
    def fixedQ(self,n):
        """Fixing computed Q by adding constant value cT"""
        return self.Q(n) + self.cT/(n*n)
    def toDictionary(self, grid): # converting result from given grid to dictionary
        """converting result from given grid to dictionary, params:
           @grid - list of given n to Test
        """
        data = {'n':[n for n in grid],
                'Q(f)':[self.Q(n) for n in grid],
                'fixedQ(f)':[self.fixedQ(n) for n in grid],
                'n^2(I(f) - Q(f))':[n*n*(self.integral - self.Q(n)) for n in grid],
                'n^2(I(f) - fixedQ(f))':[n*n*(self.integral - self.fixedQ(n)) for n in grid]}
        return data
    def dataFrame(self, grid):
        """returning DataFrame from pandas library to enhance readability"""
        print("I(f) = {} \nConstant cT = {} \nDataFrame containing results for given f:".format(self.integral,self.cT))
        return pd.DataFrame(self.toDictionary(grid))


##########################################################################################################################

# Uncomment lines which you want to test below (You can use "ctrl + /" for uncommenting/commenting several selected lines)

##########################################################################################################################

# # function f(x) = cos(x) / n in [10,100,1000,10000] / [a,b] = [0, PI]
# def f(x):
#     return np.sin(x)
# def df(x):
#     return np.cos(x)
# def F(x):
#     return -np.cos(x)
#
# quadratureTest = QuadratureTest(f = f,df = df,F = F,a = 0,b = np.pi)
# dFrame = quadratureTest.dataFrame([10,100,1000,10000])
# dFrame

##########################################################################################################################

# # simple affine function f(x) = 2x + 10 proving that there is no error there | n in [10,100,1000,10000]
# # [a,b] = [10,100]
#
# quadratureTest = QuadratureTest(f = lambda x: 2*x + 10,df = lambda x: 2,F = lambda x: x*x + 10*x ,a = 10,b =100)
# quadratureTest.dataFrame([10,100,1000,10000])


##########################################################################################################################

# # f(x) = e^x | n = [10,100,1000,10000,100000,1000000] | [a,b] = [0,1]
# quadratureTest = QuadratureTest(f = lambda x: np.exp(x),df = lambda x: np.exp(x),F = lambda x: np.exp(x),a = 0,b =1)
# quadratureTest.dataFrame([10,100,1000,10000,100000,1000000])


##########################################################################################################################


# # feel free to test your other function but remeber to compute derative and integral analytically
# # to make sure that test is reliable
#
# def f(x):
#     return None
# def df(x):
#     return None
# def F(x):
#     return None
# a = None
# b = None
# grid = None
#
# quadratureTest = QuadratureTest(f = None ,df = None, F = None, a = None,b = None)
# quadratureTest.dataFrame(grid = None)

######################################################################################################
