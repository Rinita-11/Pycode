import cmath

def _solve_quadratic_eqn_(a, b, c):
    """Calculate the solutions of the quadratic equation ax^2 + bx + c = 0."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = cmath.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    
    return x1, x2
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
try:
    solution1, solution2 = _solve_quadratic_eqn_(a, b, c)
    print(f"The solutions are: {solution1} and {solution2}")
except ValueError as e:
    print(e)
