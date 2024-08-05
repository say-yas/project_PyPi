import src.FloatNumber 
import numpy as np

class FixedPrecision:
    def __init__(self, value, decimal_places=1):
        if not isinstance(value, (int, float, src.FloatNumber.FloatNumber, np.float64, np.int64)):
            raise TypeError("Value must be an integer or float")
        if decimal_places < 0:
            raise ValueError("Number of decimal places must be non-negative")

        self.decimal_places = decimal_places
        self.value = round(value, decimal_places)

    def __eq__(self, other):
        if isinstance(other, FixedPrecision):
            return self.value == other.value
        return False

    def __add__(self, other):
        if isinstance(other, FixedPrecision):
            return FixedPrecision(self.value + other.value, max(self.decimal_places, other.decimal_places))
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return FixedPrecision(self.value + other.value, self.decimal_places)
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return FixedPrecision(self.value + other, self.decimal_places)
        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, FixedPrecision):
            return FixedPrecision(self.value - other.value, max(self.decimal_places, other.decimal_places))
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return FixedPrecision(self.value - other.value, self.decimal_places)
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return FixedPrecision(self.value - other, self.decimal_places)
        else:
            return NotImplemented
        
    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, FixedPrecision):
            return FixedPrecision(self.value * other.value, self.decimal_places + other.decimal_places)
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return FixedPrecision(self.value * other.value, self.decimal_places)
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return FixedPrecision(self.value * other, self.decimal_places)
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, FixedPrecision):
            return FixedPrecision(self.value / other.value, self.decimal_places + other.decimal_places)
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return FixedPrecision(self.value / other.value, self.decimal_places)
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return FixedPrecision(self.value / other, self.decimal_places)
        else:
            return NotImplemented
        
    def __rtruediv__(self, other):
        return self.__truediv__(other)
    
    def __pow__(self, other):
        if isinstance(other, FixedPrecision):
            return FixedPrecision(self.value ** other.value, self.decimal_places)
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return FixedPrecision(self.value ** other.value, self.decimal_places)
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return FixedPrecision(self.value ** other, self.decimal_places)
        else:
            return NotImplemented
        
    def __rpow__(self, other):
        return self.__pow__(other)
    
    def __gt__(self, other):
        if isinstance(other, FixedPrecision):
            return self.value > other.value
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return self.value > other.value
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return self.value > other
        else:
            return NotImplemented
        
    def __lt__(self, other):
        if isinstance(other, FixedPrecision):
            return self.value < other.value
        elif isinstance(other, src.FloatNumber.FloatNumber):
            return self.value < other.value
        elif isinstance(other, (int, float, np.float64, np.int64)):
            return self.value < other
        else:
            return NotImplemented
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __abs__(self):
        return FixedPrecision(abs(self.value), self.decimal_places)

    def __str__(self):
        return f"{self.value:.{self.decimal_places}f}"
    
    def __repr__(self):
        return f"FixedPrecision({self.value}, {self.decimal_places})"
