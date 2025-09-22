def calculate_remainder_and_quotient(input_number, divisor):
    quotient, remainder = divmod(input_number, divisor)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return input_number

n, m, s = map(int, input().split())

result = calculate_remainder_and_quotient(n, s) * calculate_remainder_and_quotient(m, s)

print(result)
