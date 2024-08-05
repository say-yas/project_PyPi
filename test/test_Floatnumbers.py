from src.FloatNumber import FloatNumber
from PIapprox.leibniz_pi import leibniz_pi
from PIapprox.ramanujan_pi import ramanujan_pi


pi_rama = ramanujan_pi()
print("Ramanujan approx of pi=", FloatNumber(pi_rama))

for num_terms in [1e5]:
    pi_lieb = leibniz_pi(num_terms, "FloatNumber")
    print(type(pi_lieb))
    print("Leibniz approx of pi=", pi_lieb, "for upperbound=", int(num_terms))

pi_str = "3.14159"
print("string=",pi_str, " to float: ", FloatNumber(pi_str))

pi_int = 3
print("integer=",pi_int, " to float: ", FloatNumber(pi_int))

a = FloatNumber(pi_rama)

for b in [pi_lieb, FloatNumber.tofloatnumber(pi_lieb), FloatNumber.tointnumber(pi_lieb)]:
    print("types are: ", type(a), "and", type(b))

    print("Addition: ", a + b) 
    print("Subtraction: ", a - b)  
    print("Multiplication:", a * b) 
    print("Division:", a / b)
    print("====================================")