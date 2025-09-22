def calculate_remainder_division(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values from the user
n = int(input())
m = int(input())
s = int(input())

result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

final_result = result_from_n * result_from_m

# Print the final result
print(final_result)
