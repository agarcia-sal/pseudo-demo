def multiply(num1: int, num2: int) -> int:
    digit_one = num1 - (num1 // 10) * 10
    if digit_one < 0:
        digit_one = -digit_one
    digit_two = num2 - (num2 // 10) * 10
    if digit_two < 0:
        digit_two = -digit_two
    return digit_one * digit_two