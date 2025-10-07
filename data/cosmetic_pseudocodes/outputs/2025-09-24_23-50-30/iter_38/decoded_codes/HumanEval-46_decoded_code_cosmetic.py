from typing import List


def fib4(integer_m: int) -> int:
    sliding: List[int] = [0, 0, 2, 0]

    if integer_m < 4:
        return sliding[integer_m]

    counter: int = 4
    while counter <= integer_m:
        temp: int = sum(sliding)
        sliding.append(temp)
        sliding.pop(0)
        counter += 1

    return sliding[-1]