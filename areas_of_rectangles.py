__author__ = 'dwight'

# The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width
# of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the
# same.


def main():
    rectangle_1_length = float(input('Enter the length of rectangle #1: '))
    rectangle_1_width = float(input('Enter the width of rectangle #1: '))

    print()
    rectangle_2_length = float(input('Enter the length of rectangle #2: '))
    rectangle_2_width = float(input('Enter the width of rectangle #2: '))

    print()
    compare_area_rectangle(calc_area_rectangle(rectangle_1_length, rectangle_1_width),
                           calc_area_rectangle(rectangle_2_length, rectangle_2_width))


def calc_area_rectangle(length, width):
    return length * width


def compare_area_rectangle(area1, area2):
    if area1 > area2:
        print("The area of rectangle #1 is greater.")
    elif area1 < area2:
        print("The area of rectangle #2 is greater.")
    else:
        print("The areas of the rectangles are equal.")


main()