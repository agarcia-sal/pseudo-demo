from typing import Callable


def is_multiply_prime(a: int) -> bool:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        flag: bool = True
        counter: int = 2
        while counter < n and flag:
            if n % counter == 0:
                flag = False
            counter += 1
        return flag

    first: int = 2
    while first <= 100:
        if not is_prime(first):
            first += 1
            continue
        second: int = 2
        while second <= 100:
            if not is_prime(second):
                second += 1
                continue
            third: int = 2
            while third <= 100:
                if not is_prime(third):
                    third += 1
                    continue
                if first * second * third == a:
                    return True
                third += 1
            second += 1
        first += 1
    return False