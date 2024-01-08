#python program to solve quadratic equation ax**2 +bx +c = 0
import cmath
print("Enter the coefficients of the equation")
a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
d = (b**2)-(4*a*c)

#finding two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The two solutions are {0},{1}".format(sol1,sol2))


