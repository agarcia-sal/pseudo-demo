def greatest_common_divisor(a, b):
    while b != 0:
        temporary = b
        b = a % b
        a = temporary
    return a