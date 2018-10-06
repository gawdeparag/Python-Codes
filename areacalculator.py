def triangle_area(base, height):
    area = 0.5 * base * height
    return area

def square_area(side):
    area = side ** 2
    return area

def rectangle_area(length, width):
    area = length * width
    return area

while True:
    print("1. Area of Triangle")
    print("2. Area of Square")
    print("3. Area of Rectangle")
    print("4. Exit")
    option = int(input("Enter your option: "))
    if option == 1:
        base = float(input("Enter base of the triangle: "))
        height = float(input("Enter height of the triangle: "))
        print("Area of the triangle: ", triangle_area(base, height))
    elif option == 2:
        side = float(input("Enter the side of the square: "))
        print("Area of square:", square_area(side))
    elif option == 3:
        length = float(input("Enter the length of the Rectangle: "))
        width = float(input("Enter the width of the Rectangle: "))
        print("Area of the rectangle: ", rectangle_area(length, width))
    elif option == 4:
        break
    else:
        print("Invalid Option!")

