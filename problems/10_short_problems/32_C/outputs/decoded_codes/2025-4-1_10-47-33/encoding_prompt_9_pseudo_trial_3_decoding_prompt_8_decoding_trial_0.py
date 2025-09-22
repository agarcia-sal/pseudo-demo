def calculate_modified_value(number, divisor):
    quotient = number // divisor
    remainder = number % divisor
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

value1 = int(input())
value2 = int(input())
divider = int(input())

modified_value1 = calculate_modified_value(value1, divider)
modified_value2 = calculate_modified_value(value2, divider)

result = modified_value1 * modified_value2
print(result)
