def calculate_adjusted_value(value, divisor):
    quotient = value // divisor
    remainder = value % divisor
    if remainder > 0:
        return remainder * quotient + 1
    else:
        return value

# Read Input Values
n, m, s = input().split()
n = int(n)
m = int(m)
s = int(s)

# Calculate Adjusted Values
adjusted_n = calculate_adjusted_value(n, s)
adjusted_m = calculate_adjusted_value(m, s)

# Calculate Product
result = adjusted_n * adjusted_m

# Output Result
print(result)
