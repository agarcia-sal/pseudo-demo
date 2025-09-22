def calculate_remainder_division(number, divisor):
    quotient = number // divisor  # Integer division for the quotient
    remainder = number % divisor    # Modulus operator for remainder
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Reading input values from the user
n = int(input())
m = int(input())
s = int(input())

result_from_n = calculate_remainder_division(n, s)
result_from_m = calculate_remainder_division(m, s)

FINAL_RESULT = result_from_n * result_from_m

print(FINAL_RESULT)
