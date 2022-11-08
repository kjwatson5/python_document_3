import math

def house_square_footage():
    lenth_of_house = input('Enter the length of the hosue in feet: ')
    width_of_house = input('Enter the width of the house in feet: ')
    square_feet = int(lenth_of_house) + int(width_of_house)

    return square_feet

def circumference_of_circle():
    diameter = input('What is the diameter of the circle? ')
    circle_circumference = int(diameter) * math.pi
    return circle_circumference
