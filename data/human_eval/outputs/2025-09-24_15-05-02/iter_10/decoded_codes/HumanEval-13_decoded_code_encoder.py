def greatest_common_divisor(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a