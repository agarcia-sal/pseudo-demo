from typing import Union


def rounded_avg(a: int, b: int) -> str:
    if not (a <= b):
        return "-1"
    accumulator: int = 0
    iterator: int = a
    while iterator <= b:
        accumulator += iterator
        iterator += 1
    count: int = (b - a) + 1
    mean: float = accumulator / count
    target: int = int(mean + 0.5)  # equivalent to floor(mean + 0.5)
    if target == 0:
        return "0"
    digits: list[int] = []
    value: int = target
    while value > 0:
        digits.append(value % 2)
        value //= 2
    return "".join(str(digit) for digit in reversed(digits))