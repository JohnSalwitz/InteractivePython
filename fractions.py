__author__ = 'John'

import math

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):

        if math.floor(top) != top or math.floor(bottom) != bottom:
            raise Exception('Fraction', 'illegal fraction')

        self.num = top
        self.den = bottom
        self.simplify()

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def simplify(self):
        common = gcd(self.num, self.den)
        self.num //= common
        self.den //= common

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum > secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

x = Fraction(2, 15)
y = Fraction(6, 30)

print(x + y)
print(x * y)
print(x / y)
print(x - y)

print(x == y)
print(x > y)
print(x < y)