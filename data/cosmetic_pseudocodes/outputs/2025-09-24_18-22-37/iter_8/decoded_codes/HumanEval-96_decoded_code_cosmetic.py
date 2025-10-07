from typing import List

def count_up_to(m: int) -> List[int]:
    result_list: List[int] = []
    p: int = 2
    while p < m:
        prime_flag: bool = True
        q: int = 2
        while q < p:
            if p % q == 0:
                prime_flag = False
                break
            q += 1
        if prime_flag:
            result_list.append(p)
        p += 1
    return result_list