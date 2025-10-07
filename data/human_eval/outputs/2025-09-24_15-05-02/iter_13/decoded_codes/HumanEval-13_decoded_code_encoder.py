def greatest_common_divisor(a, b):
    while b != 0:
        temp_a = b
        temp_b = a % b
        a = temp_a
        b = temp_b
    return a