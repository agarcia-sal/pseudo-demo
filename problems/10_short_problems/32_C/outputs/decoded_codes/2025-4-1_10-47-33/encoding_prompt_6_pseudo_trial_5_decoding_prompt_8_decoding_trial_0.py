def calculate_remainder_count(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

n = int(input())
m = int(input())
s = int(input())

adjusted_count_for_n = calculate_remainder_count(n, s)
adjusted_count_for_m = calculate_remainder_count(m, s)

result = adjusted_count_for_n * adjusted_count_for_m

print(result)
