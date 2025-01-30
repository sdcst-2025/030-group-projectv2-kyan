#!python3
# Volume Calculator
# Feel free to rename your variables

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return "Welcome to calculator 9000! This calculator can calculate area of certain shapes, convert measurements, and find the volume of certain 3D shapes"

def circle(r):
    pi = 3.141592653
    answer = pi*r**2
    return answer

def circlesolve():
    r = float(input("Enter the radius of your circle: "))
    print(circle(r))

def triangle(b, h):
    answer = (1/2) * b * h
    return answer

def trianglesolve():
    b = float(input("Enter the base length of your triangle: "))
    h = float(input("Enter the height length of your triangle: "))
    print(triangle(b,h))

def square(l):
    answer =  l**2
    return answer

def squaresolve():
    l = float(input("Enter your squares side length: "))
    print(square(l))

def rectangle(l, w):
    answer = l * w
    return answer

def rectanglesolve():
    l = float(input("Enter your rectangles length: "))
    w = float(input("Enter your rectangles width: "))
    print(rectangle(l,w))

def cm_m(x):
    answer = x/100
    return answer

def cm_m_solve():
    x = float(input("Input your number of cm to convert to metres: "))
    print(cm_m(x))

def m_km(x):
    answer = x/1000
    return answer

def m_km_solve():
    x = float(input("Enter the amount of metres to convert to km: "))
    print(m_km(x))

def km_miles(x):
    answer = x/1.609
    return answer

def km_miles_solve():
    x = float(input("Enter the amount of km to convert to miles: "))
    print(km_miles(x))

def cube(l):
    answer = l**3
    return answer

def cube_solve():
    l = float(input("Enter the side length of your cube: "))
    print(cube(l))

def cylinder(r, h):
    pi = 3.141592653
    answer = pi * (r**2) * h
    return answer

def cylinder_solve(r,h):
    r = float(input("Enter the radius of your cylinder: "))
    h = float(input("Enter the height of your cylinder: "))
    print(cylinder(r,h))

def sphere(r):
    pi = 3.141592653
    answer = (4/3)*pi*(r**3)
    return answer

def sphere_solve(r):
    r = float(input("Enter the radius of your sphere: "))
    print(sphere(r))

def pyramid(l,w,h):
    answer = (l*w*h)/3
    return answer

def pyramid_solve():
    l = float(input("Enter the length of your pyramid: "))
    w = float(input("Enter the width of your pyramid: "))
    h = float(input("Enter the height of your pyramid: "))
    print(pyramid(l,w,h))

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return "To begin, enter what you want to calculate, you can enter C for area of circle, T for area of triangle, S for area of square, R for area of rectangle, CM for converting cm to metres, M for converting metres to km, KM for converting km to miles, CU for volume of a cube, CY for volume of a cylinder, SP for volume of a sphere, and P for volume of a pyramid"



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    cont = True
    print(title())
    while cont == True:
        # keep giving options to choose menu options until they choose to exit
        choice = (input("Enter what you want to calculate: "))
        if choice == "C":
            circlesolve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "T":
            trianglesolve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False
        
        elif choice == "S":
            squaresolve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "R":
            rectanglesolve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "CM":
            cm_m_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "M":
            m_km_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "KM":
            km_miles_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "CU":
            cube_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "CY":
            cylinder_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "SP":
            sphere_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

        elif choice == "P":
            pyramid_solve()
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

if __name__ == "__main__":
    main()
