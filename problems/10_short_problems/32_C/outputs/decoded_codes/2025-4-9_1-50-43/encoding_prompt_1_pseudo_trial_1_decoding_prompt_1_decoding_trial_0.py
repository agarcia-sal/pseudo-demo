def calculate_modified_value(original_number, divisor):
    quotient = original_number // divisor       # Integer division to get quotient
    remainder = original_number % divisor       # Modulo operation to get remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else: 
        return original_number

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate modified values for n and m using the divisor s
modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)

# Calculate and print the final result as the product of modified_n and modified_m
print(modified_n * modified_m)
