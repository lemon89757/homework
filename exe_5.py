import math
def quadratic_equation(a,b,c):
    characteristic_equation = b*b-4*a*c
    if characteristic_equation<0:
        x1=x2='no solution'
        return x1,x2
    elif characteristic_equation==0:
        x1=x2=-(b/(2*a))
        return x1,x2
    else:
        sqrt_characteristic_equation = math.sqrt(characteristic_equation)
        x1 = (-b + sqrt_characteristic_equation)/(2*a)
        x2 = (-b - sqrt_characteristic_equation)/(2*a)
        return x1, x2

print(quadratic_equation(a= int(input("a=")),b= int(input("b=")),c= int(input("c="))))



