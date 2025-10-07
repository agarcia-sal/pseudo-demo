from typing import List


def count_up_to(m: int) -> List[int]:
    prime_collection: List[int] = []
    k: int = 2
    while k < m:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < k and prime_flag:
            if k % divisor == 0:
                prime_flag = False
            else:
                divisor += 1
        if prime_flag:
            prime_collection.append(k)
        k += 1
    return prime_collection