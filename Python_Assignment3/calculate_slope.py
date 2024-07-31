def calculate_slope(x1, y1, x2, y2):
    """Calculate the slope of the line passing through (x1, y1) and (x2, y2)."""
    if x1 == x2:
        raise ValueError("Cannot calculate slope: The x-coordinates are the same, leading to a vertical line.")
    
    slope = (y2 - y1) / (x2 - x1)
    return slope
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
try:
    slope = calculate_slope(x1, y1, x2, y2)
    print(f"The slope of the line is {slope}.")
except ValueError as e:
    print(e)
