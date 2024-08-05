from src.FixedPrecision  import FixedPrecision
from src.FloatNumber import FloatNumber


print("\nfixedprecison (op) fixedprecison:\n")

a = FixedPrecision(3.14159, 2)
b = FixedPrecision(2.71828, 3)

print(a)      
print(b)      
print(a + b)  
print(a - b)  
print(a * b)  
print(a / b)  

print("\nfixedprecison (op) FloatNumber:\n")
a = FixedPrecision(2.71828, 3)
b = FloatNumber(3.14159)

print(a)      
print(b)      
print(a + b)  
print(a - b) 
print(a * b)  
print(a / b)  

print("\nFloatnumber (op) fixedpoint:\n")
a = FloatNumber(3.14159)
b = FixedPrecision(2.71828, 3)


print(a)      
print(b)      
print(a + b)  
print(a - b) 
print(a * b)  
print(a / b)  

print("\nfixedprecison (op) int: \n")
a = FixedPrecision(2.71828, 3)
b = 7

print(a)      
print(b)      
print(a + b)  
print(a - b) 
print(a * b)  
print(a / b)  
