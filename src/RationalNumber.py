import numpy as np
import src.FixedPrecision
import src.FloatNumber 

class RationalNumber:
    """
    Class to represent a rational number.
    """
    def __init__(self, numerator, denominator=1):
        if not isinstance(numerator, (int,np.int64)) or not isinstance(denominator, (int,np.int64)):
            print(type(numerator), type(denominator))
            raise TypeError("Both numerator and denominator must be integers")
        if denominator == 0:
            raise ZeroDivisionError("Denominator must be nonzero")
        
        # Add normalization for further simplification of the fraction
        g = np.gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __eq__(self, other):
        if isinstance(other, RationalNumber):
            return self.numerator*other.denominator == self.denominator*other.numerator
        ## a/b == c/d if a*d == b*c
        return False
    
    def __add__(self, other):
        if isinstance(other, RationalNumber):
            nume = self.numerator * other.denominator + other.numerator * self.denominator
            denome = self.denominator * other.denominator

            g = np.gcd(nume, denome)
            new_nume = nume // g
            new_denome = denome // g

            return RationalNumber(int(new_nume), int(new_denome))
        elif isinstance(other, int):
            print(other)
            return RationalNumber(int(self.numerator + other * self.denominator), int(self.denominator))
        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if isinstance(other, RationalNumber):
            nume = self.numerator * other.denominator - other.numerator * self.denominator
            denome = self.denominator * other.denominator

            g = np.gcd(nume, denome)
            new_nume = nume // g
            new_denome = denome // g

            return RationalNumber(int(new_nume), int(new_denome))
        elif isinstance(other, int):
            return RationalNumber(int(self.numerator - other * self.denominator), int(self.denominator))
        else:
            return NotImplemented
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __mul__(self, other):
        if isinstance(other, RationalNumber):
            nume = self.numerator * other.numerator
            denome = self.denominator * other.denominator
        
            g = np.gcd(nume, denome)
            new_nume = nume // g
            new_denome = denome // g

            return RationalNumber(int(new_nume), int(new_denome))
        elif isinstance(other, int):
            return RationalNumber(int(self.numerator * other), int(self.denominator))
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, RationalNumber):
            nume = self.numerator * other.denominator
            denome = self.denominator * other.numerator

            g = np.gcd(nume, denome)
            new_nume = nume // g
            new_denome = denome // g

            return RationalNumber(int(new_nume), int(new_denome))
        elif isinstance(other, int):
            return RationalNumber(int(self.numerator), int(self.denominator * other))
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __invert__(self):
        return RationalNumber(self.denominator, self.numerator)

    def __gt__(self, other):
        if isinstance(other, RationalNumber):
            return self.numerator*other.denominator > self.denominator*other.numerator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, RationalNumber):
            return self.numerator*other.denominator < self.denominator*other.numerator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            return NotImplemented

    def __abs__(self):
        return RationalNumber(abs(self.numerator), abs(self.denominator))
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"
    
    def tofloatnumber(self):
        return src.FloatNumber.FloatNumber( self.numerator / self.denominator )
    
    def tofloat(self):
        return float( self.numerator / self.denominator )
    
    def tofixedprecision(self, precision=2):
        return src.FixedPrecision.FixedPrecision( self.numerator / self.denominator , precision)
    
    



