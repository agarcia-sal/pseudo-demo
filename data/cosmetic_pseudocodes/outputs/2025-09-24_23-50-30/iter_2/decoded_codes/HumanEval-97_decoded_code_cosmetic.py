from typing import Callable


def multiply(integer_a: int, integer_b: int) -> int:
    result: int = 0

    def helper(x: int, y: int) -> int:
        if x == 0:
            return 0
        else:
            return 1 + helper(x - 1, y)

    digit_a: int = 0
    digit_b: int = 0

    while True:
        if integer_a == 0:
            break
        digit_a = abs(integer_a - (integer_a // 10) * 10)
        break

    while True:
        if integer_b == 0:
            break
        digit_b = abs(integer_b - (integer_b // 10) * 10)
        break

    if digit_a == 0:
        return 0
    elif digit_b == 0:
        return 0
    else:
        acc: int = 0
        count: int = 0
        while count < digit_b:
            acc += digit_a
            count += 1
        return acc