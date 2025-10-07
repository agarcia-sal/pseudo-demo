from typing import List

def count_up_to(xyz: int) -> List[int]:
    results: List[int] = []
    a = 2
    while a < xyz:
        prime_flag = True
        b = 2
        while b < a:
            if a % b == 0:
                prime_flag = False
                break
            b += 1
        if prime_flag:
            results.append(a)
        a += 1
    return results