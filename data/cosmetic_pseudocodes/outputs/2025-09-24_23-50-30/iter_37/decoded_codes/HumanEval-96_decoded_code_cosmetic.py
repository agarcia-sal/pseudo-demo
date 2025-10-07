from typing import List


def count_up_to(p: int) -> List[int]:
    result: List[int] = []
    k: int = 2
    while k < p:
        prime_flag: bool = True
        m: int = 2
        while m < k and prime_flag:
            if k % m == 0:
                prime_flag = False
            else:
                m += 1
        if prime_flag:
            result.append(k)
        k += 1
    return result