def calculate_modified_value(total, divisor):
    quotient = total // divisor  # Calculate the quotient
    remainder = total % divisor   # Calculate the remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Return modified value if there is a remainder
    else:
        return total  # Return original total if no remainder

# Main program
n = int(input())  # Read integer value for n
m = int(input())  # Read integer value for m
s = int(input())  # Read integer value for s

modified_n = calculate_modified_value(n, s)  # Calculate modified value for n
modified_m = calculate_modified_value(m, s)  # Calculate modified value for m

final_result = modified_n * modified_m  # Calculate final product
print(final_result)  # Output the final result
