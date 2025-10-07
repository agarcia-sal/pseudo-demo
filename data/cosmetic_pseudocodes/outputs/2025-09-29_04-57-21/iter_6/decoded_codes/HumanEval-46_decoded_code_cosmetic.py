from typing import List

def fib4(integer_n: int) -> int:
    recentValues: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return recentValues[integer_n]

    counter = 4
    while counter <= integer_n:
        sumLatestFour = sum(recentValues)
        recentValues.append(sumLatestFour)
        recentValues.pop(0)  # maintain last 4 values
        counter += 1

    return recentValues[3]