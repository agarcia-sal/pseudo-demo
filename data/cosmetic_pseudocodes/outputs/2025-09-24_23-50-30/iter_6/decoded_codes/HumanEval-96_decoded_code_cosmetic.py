from typing import List

def count_up_to(p: int) -> List[int]:
    primes_list: List[int] = []
    x: int = 2
    while x < p:
        prime_flag: int = 1
        y: int = 2
        while y < x and prime_flag != 0:
            if x % y == 0:
                prime_flag = 0
            y += 1
        if prime_flag == 1:
            primes_list.append(x)
        x += 1
    return primes_list