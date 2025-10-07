from typing import List

def count_up_to(non_negative_integer_n: int) -> List[int]:
    list_of_primes: List[int] = []
    for integer_i in range(2, non_negative_integer_n):
        is_prime_flag = True
        for integer_j in range(2, integer_i):
            if integer_i % integer_j == 0:
                is_prime_flag = False
                break
        if is_prime_flag:
            list_of_primes.append(integer_i)
    return list_of_primes