from typing import List


def count_up_to(limit: int) -> List[int]:
    primes_collection: List[int] = []
    i_counter: int = 2
    while i_counter < limit:
        prime_flag: bool = True
        j_iter: int = 2
        while j_iter < i_counter:
            if i_counter % j_iter == 0:
                prime_flag = False
                j_iter = i_counter  # Exit inner loop early
            else:
                j_iter += 1
        if prime_flag:
            primes_collection.append(i_counter)
        i_counter += 1
    return primes_collection