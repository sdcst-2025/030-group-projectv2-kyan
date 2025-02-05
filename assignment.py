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
    return "\033[0;32m\033[1m\033[4mWelcome to calculator 9000! This calculator can calculate area of certain shapes, convert measurements, and find the volume of certain 3D shapes\033[0m"

def circle(r):
    pi = 3.141592653
    answer = pi*r**2
    return answer

def circlesolve():
    r = float(input("Enter the radius of your circle: "))
    if r > 0:
        print(circle(r))
    else:
        print("Invalid Input")

def triangle(b, h):
    answer = (1/2) * b * h
    return answer

def trianglesolve():
    b = float(input("Enter the base length of your triangle: "))
    h = float(input("Enter the height length of your triangle: "))
    if b > 0 and h > 0:
        print(triangle(b,h))
    else:
        print("Invalid Input")

def square(l):
    answer =  l**2
    return answer

def squaresolve():
    l = float(input("Enter your squares side length: "))
    if l > 0:
        print(square(l))
    else:
        print("Invalid Input")

def rectangle(l, w):
    answer = l * w
    return answer

def rectanglesolve():
    l = float(input("Enter your rectangles length: "))
    w = float(input("Enter your rectangles width: "))
    if l > 0 and w > 0:
        print(rectangle(l,w))
    else:
        print("Invalid Input")

def cm_m(x):
    answer = x/100
    return answer

def cm_m_solve():
    x = float(input("Input your number of cm to convert to metres: "))
    if x > 0:
        print(cm_m(x))
    else:
        print("Invalid Input")

def m_km(x):
    answer = x/1000
    return answer

def m_km_solve():
    x = float(input("Enter the amount of metres to convert to km: "))
    if x > 0:
        print(m_km(x))
    else:
        print("Invalid Input")

def km_miles(x):
    answer = x/1.609
    return answer

def km_miles_solve():
    x = float(input("Enter the amount of km to convert to miles: "))
    if x > 0:
        print(km_miles(x))
    else:
        print("Invalid Input")

def cube(l):
    answer = l**3
    return answer

def cube_solve():
    l = float(input("Enter the side length of your cube: "))
    if l > 0:
        print(cube(l))
    else:
        print("Invalid Input")

def cylinder(r, h):
    pi = 3.141592653
    answer = pi * (r**2) * h
    return answer

def cylinder_solve(r,h):
    r = float(input("Enter the radius of your cylinder: "))
    h = float(input("Enter the height of your cylinder: "))
    if r > 0 and h > 0:
        print(cylinder(r,h))
    else:
        print("Invalid Input")

def sphere(r):
    pi = 3.141592653
    answer = (4/3)*pi*(r**3)
    return answer

def sphere_solve():
    r = float(input("Enter the radius of your sphere: "))
    if r > 0:
        print(sphere(r))
    else:
        print("Invalid Input")

def pyramid(l,w,h):
    answer = (l*w*h)/3
    return answer

def pyramid_solve():
    l = float(input("Enter the length of your pyramid: "))
    w = float(input("Enter the width of your pyramid: "))
    h = float(input("Enter the height of your pyramid: "))
    if l > 0 and w > 0 and h > 0:
        print(pyramid(l,w,h))
    else:
        print("Invalid Input")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:

    ques = [
        ['\033[1;33mC','\033[1;33mArea of Circle'],
        ['\033[0;32mT','\033[0;32mArea of Triangle'],
        ['\033[0;34mS','\033[0;34mArea of Square'],
        ['\033[0;35mR','\033[0;35mArea of Rectangle'],
        ['\033[0;36mCM','\033[0;36mConvert CM to M'],
        ['\033[1;31mM','\033[1;31mConvert M to KM'],
        ['\033[1;32mKM','\033[1;32mConvert KM to MI'],
        ['\033[1;34mCU','\033[1;34mVolume of Cube'],
        ['\033[1;35mCY','\033[1;35mVolume of Cylinder'],
        ['\033[1;36mSP','\033[1;36mVolume of Sphere'],
        ['\033[0;33mP','\033[0;33mVolume of Pyramid'],

    ]

    for i in ques:
        print(f"{i[0]:<10}- {i[1]:<12}")

    return "\033[0;31m\033[1mTo begin, enter what you want to calculate\033[0m"


"""
    \0331;33mC, for area of circle\0330m
    \033[0;32mT for area of triangle\033[0m 
    \033[0;34mS for area of square\033[0m 
    \033[0;35mR for area of rectangle\033[0m 
    \033[0;36mCM for converting cm to metres\033[0m 
    \033[1;31mM for converting metres to km\033[0m 
    \033[1;32mKM for converting km to miles\033[0m 
    \033[1;34mCU for volume of a cube\033[0m 
    \033[1;35mCY for volume of a cylinder\033[0m 
    \033[1;36mSP for volume of a sphere\033[0m 
    \033[0;33mand P for volume of a pyramid\033[0m
"""


def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    cont = True
    print(title())
    print(instructions())
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
        else:
            print("Invalid Input")
            ask = input("Would you like to calculate something else? (Type Y or N): ")
            if ask == "Y":
                cont = True
            else:
                cont = False

if __name__ == "__main__":
    main()
