def greatest_common_divisor(a, b):
    while b != 0:
        temp_a = b
        b = a % b
        a = temp_a
    return a