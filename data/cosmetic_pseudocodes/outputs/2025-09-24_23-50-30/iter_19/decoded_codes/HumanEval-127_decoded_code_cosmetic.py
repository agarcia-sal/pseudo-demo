from typing import Sequence

def intersection(argA: Sequence[int], argB: Sequence[int]) -> str:
    def is_prime(num: int) -> bool:
        if num <= 1:
            return False
        if num == 2:
            return True
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    p: int = argA[0] if argA[0] > argB[0] else argB[0]
    q: int = argA[1] if argA[1] < argB[1] else argB[1]
    length: int = q - p

    if length > 0 and is_prime(length):
        return "YES"
    return "NO"