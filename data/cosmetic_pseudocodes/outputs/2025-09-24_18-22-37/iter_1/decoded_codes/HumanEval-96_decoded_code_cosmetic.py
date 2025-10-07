from typing import List

def count_up_to(n: int) -> List[int]:
    primes: List[int] = []
    for i in range(2, n):
        prime_flag = True
        for j in range(2, i):
            if i % j == 0:
                prime_flag = False
                break
        if prime_flag:
            primes.append(i)
    return primes