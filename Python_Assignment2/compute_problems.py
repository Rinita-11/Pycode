import math

def compute_operations():
   
    power_result = 5 ** 8
    sqrt_result = math.sqrt(400)
    exp_result = math.exp(5)
    log_result = math.log(625, 5)
    
    return power_result, sqrt_result, exp_result, log_result
power_result, sqrt_result, exp_result, log_result = compute_operations()

print(f"5 to the power of 8 is: {power_result}")
print(f"Square root of 400 is: {sqrt_result}")
print(f"Exponent of 5 (e^5) is: {exp_result}")
print(f"Logarithm of 625 with base 5 is: {log_result}")
