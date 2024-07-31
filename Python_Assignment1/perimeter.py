import math

def rectangle_properties(width, height):
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

def circle_properties(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Example usage:
width = 5
height = 10
rectangle_area, rectangle_perimeter = rectangle_properties(width, height)
print(f"Rectangle - Area: {rectangle_area}, Perimeter: {rectangle_perimeter}")

radius = 7
circle_area, circle_circumference = circle_properties(radius)
print(f"Circle - Area: {circle_area}, Circumference: {circle_circumference}")
