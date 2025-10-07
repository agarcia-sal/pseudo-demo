from typing import List

def factorize(integer_n: int) -> List[int]:
    list_of_factors: List[int] = []
    divisor = 2
    while divisor * divisor <= integer_n + 1:
        while integer_n % divisor == 0:
            list_of_factors.append(divisor)
            integer_n //= divisor
        divisor += 1
    if integer_n > 1:
        list_of_factors.append(integer_n)
    return list_of_factors