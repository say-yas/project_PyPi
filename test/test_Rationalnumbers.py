from src.RationalNumber import RationalNumber

a = RationalNumber(3, 10)
b = RationalNumber(4, 5)
print(a,b)
print("types are: ", type(a), "and", type(b))

print("Addition: ", a + b) 
print("Subtraction: ", a - b)  
print("Multiplication:", a * b) 
print("Division:", a / b) 



a = 8
b = RationalNumber(7,4)
print(a,b)
print("types are: ", type(a), "and", type(b))

print("Addition: ", a + b) 
print("Subtraction: ", a - b)  
print("Multiplication:", a * b) 
print("Division:", a / b) 

print(b.tofloatnumber())
print(b.tofixedprecision(4))
