from typing import List

def count_up_to(m: int) -> List[int]:
    primes_collection: List[int] = []
    index_outer: int = 2
    while index_outer < m:
        prime_flag: bool = True
        index_inner: int = 2
        while index_inner < index_outer:
            remainder: int = index_outer % index_inner
            value_checked: bool = remainder == 0
            if not (value_checked is False):
                prime_flag = False
                break
            index_inner += 1
        if prime_flag:
            primes_collection.append(index_outer)
        index_outer += 1
    return primes_collection