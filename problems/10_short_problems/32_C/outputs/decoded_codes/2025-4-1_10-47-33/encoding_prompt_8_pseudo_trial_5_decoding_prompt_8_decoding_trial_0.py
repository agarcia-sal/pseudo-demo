def calculate_modified_value(total, divisor):
    quotient = total // divisor
    remainder = total % divisor
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Main Program
n = int(input())
m = int(input())
s = int(input())

modified_n = calculate_modified_value(n, s)
modified_m = calculate_modified_value(m, s)
final_result = modified_n * modified_m

print(final_result)
