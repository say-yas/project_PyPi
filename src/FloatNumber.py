import src.FixedPrecision
import numpy as np
class FloatNumber:
    """
    A class to perform arithmetic operations on float numbers
    """
    def __init__(self, value):

        if isinstance(value, float):
            self.value = value
        elif isinstance(value, str):
            self.value = float(value)
        elif isinstance(value, (int, np.int64)):
            self.value = float(value)
        else:
            raise TypeError("Value must be a string, integer, or float")
        
    def __eq__(self, other):
        if isinstance(other, FloatNumber):
            return self.value == other.value
        return False

    def __add__(self, other):
        
        if isinstance(other, FloatNumber):
            return  FloatNumber( self.value + other.value )
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return  FloatNumber( self.value + other.value )
        elif isinstance(other, float):
            return  FloatNumber( self.value + other )
        elif isinstance(other, str):
            return  FloatNumber( self.value + float(other) )
        elif isinstance(other, (int, np.int64)):
            return  FloatNumber( self.value + float(other) )
        else:
            return  NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):

        if isinstance(other, FloatNumber):
            return  FloatNumber( self.value - other.value )
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return  FloatNumber( self.value - other.value )
        elif isinstance(other, float):
            return  FloatNumber( self.value - other )
        elif isinstance(other, str):
            return  FloatNumber( self.value - float(other) )
        elif isinstance(other, (int, np.int64)):
            return  FloatNumber( self.value - float(other) )
        else:
            return  NotImplemented
        
    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, FloatNumber):
            return  FloatNumber( self.value * other.value )
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return  FloatNumber( self.value * other.value )
        elif isinstance(other, float):
            return  FloatNumber( self.value * other )
        elif isinstance(other, str):
            return  FloatNumber( self.value * float(other) )
        elif isinstance(other, (int, np.int64)):
            return  FloatNumber( self.value * float(other) )
        else:
            return  NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, FloatNumber):
            return  FloatNumber( self.value / other.value )
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return  FloatNumber( self.value / other.value )
        elif isinstance(other, float):
            return  FloatNumber( self.value / other)
        elif isinstance(other, str):
            return  FloatNumber( self.value / float(other) )
        elif isinstance(other, (int, np.int64)):
            return  FloatNumber( self.value / float(other) )
        else:
            return  NotImplemented
        
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __pow__(self, other):
        if isinstance(other, FloatNumber):
            return  FloatNumber( self.value ** other.value )
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return  FloatNumber( self.value ** other.value )
        elif isinstance(other, float):
            return  FloatNumber( self.value ** other)
        elif isinstance(other, str):
            return  FloatNumber( self.value ** float(other) )
        elif isinstance(other, (int, np.int64)):
            return  FloatNumber( self.value ** float(other) )
        else:
            return  NotImplemented
    
    def __rpow__(self, other):
        return self.__pow__(other)
        
    def __abs__(self):
        return FloatNumber( abs(self.value) )
        
    def __str__(self):
        return str(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):      
        return int(self.value)
    
    def __gt__(self, other):
        if isinstance(other, FloatNumber):
            return self.value > other.value
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return self.value > other.value
        elif isinstance(other, float):
            return self.value > other
        elif isinstance(other, str):
            return self.value > float(other)
        elif isinstance(other, (int, np.int64)):
            return self.value > float(other)
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, FloatNumber):
            return self.value < other.value
        elif isinstance(other, src.FixedPrecision.FixedPrecision):
            return self.value < other.value
        elif isinstance(other, float):
            return self.value < other
        elif isinstance(other, str):
            return self.value < float(other)
        elif isinstance(other, (int, np.int64)):
            return self.value < float(other)
        else:
            return NotImplemented
    
    def tofloatnumber(self):
        return float( self.value)
    
    def tointnumber(self):
        return int( self.value)
    
    def tofixedprecision(self, precision=2):
        return src.FixedPrecision.FixedPrecision( self.value , precision)

    def __repr__(self):
        return f"FloatNumber({self.value})"

