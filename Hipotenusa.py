import math

cateto1 = float(input("Introduce el primer cateto: "))
cateto2 = float(input("Introduce el segundo cateto: "))

h = math.sqrt(cateto1**2 + cateto2**2)

print("La hipotenusa del triángulo es:", h)