from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        divisor = 2
        while divisor * divisor <= n:
            if n % divisor == 0:
                return False
            divisor += 1
        return True

    firstFactor = 2
    while firstFactor <= 100:
        if not is_prime(firstFactor):
            firstFactor += 1
            continue

        secondFactor = 2
        while secondFactor <= 100:
            if not is_prime(secondFactor):
                secondFactor += 1
                continue

            thirdFactor = 2
            while thirdFactor <= 100:
                if not is_prime(thirdFactor):
                    thirdFactor += 1
                    continue

                if firstFactor * secondFactor * thirdFactor == a:
                    return True

                thirdFactor += 1

            secondFactor += 1

        firstFactor += 1

    return False