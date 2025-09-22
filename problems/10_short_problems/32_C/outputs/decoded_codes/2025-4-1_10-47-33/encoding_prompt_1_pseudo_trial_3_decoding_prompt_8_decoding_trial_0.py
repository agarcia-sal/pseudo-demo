def calculate_remainder_and_adjustment(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

n = int(input())
m = int(input())
s = int(input())

RESULT_A = calculate_remainder_and_adjustment(n, s)
RESULT_B = calculate_remainder_and_adjustment(m, s)

FINAL_RESULT = RESULT_A * RESULT_B

print(FINAL_RESULT)
