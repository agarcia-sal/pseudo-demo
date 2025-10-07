from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def isPrime(number: int) -> bool:
        if number < 2:
            return False
        limit = int(number**0.5)
        for divisor in range(2, limit + 1):
            if number % divisor == 0:
                return False
        return True

    maxx: int = 0
    i: int = 0
    length: int = len(list_of_integers)

    while i < length:
        value = list_of_integers[i]
        if value > maxx and isPrime(value):
            maxx = value
        i += 1

    # Sum digits of maxx except the last digit, handle maxx=0 (no digits summed, result=0)
    maxx_str = str(maxx)
    result: int = sum(int(d) for d in maxx_str[:-1]) if len(maxx_str) > 1 else 0

    return result