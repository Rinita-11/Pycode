import math

def compute_trigonometric_functions():

    sin_60_degrees = math.sin(math.radians(60))
    cos_pi = math.cos(math.pi)
    sin_value = math.sin(0.8660254037844386)
    tan_90_degrees = math.tan(math.radians(90))
    
    return sin_60_degrees, cos_pi, sin_value, tan_90_degrees
sin_60_degrees, cos_pi, sin_value, tan_90_degrees = compute_trigonometric_functions()

print(f"sin(60 degrees) is: {sin_60_degrees}")
print(f"cos(π radians) is: {cos_pi}")
print(f"sin(0.8660254037844386) is: {sin_value}")
print(f"tan(90 degrees) is: {tan_90_degrees}")
