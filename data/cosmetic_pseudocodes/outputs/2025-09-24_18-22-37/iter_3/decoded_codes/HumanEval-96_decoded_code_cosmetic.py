from typing import List

def count_up_to(n: int) -> List[int]:
    primesList: List[int] = []

    def check_prime(x: int, divisor: int) -> bool:
        if divisor * divisor > x:
            return True
        if x % divisor == 0:
            return False
        return check_prime(x, divisor + 1)

    current: int = 2
    while current < n:
        if check_prime(current, 2):
            primesList.append(current)
        current += 1
    return primesList