from typing import List


def count_up_to(limit: int) -> List[int]:
    primes_collection: List[int] = []
    index: int = 2
    while index < limit:
        flag: bool = True
        divisor: int = 2
        while divisor * divisor <= index and flag:
            if index % divisor == 0:
                flag = False
            divisor += 1
        if flag:
            primes_collection.append(index)
        index += 1
    return primes_collection