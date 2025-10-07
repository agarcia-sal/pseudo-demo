from typing import List

def count_up_to(n: int) -> List[int]:
    primes_collection: List[int] = []
    current_num: int = 2
    while current_num < n:
        prime_flag: bool = True
        divisor_candidate: int = 2
        while divisor_candidate < current_num:
            if current_num % divisor_candidate == 0:
                prime_flag = False
                break
            divisor_candidate += 1
        if prime_flag:
            primes_collection.append(current_num)
        current_num += 1
    return primes_collection