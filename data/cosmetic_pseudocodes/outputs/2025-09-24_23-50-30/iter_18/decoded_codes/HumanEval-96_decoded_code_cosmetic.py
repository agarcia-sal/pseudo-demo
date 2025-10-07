from typing import List


def count_up_to(m: int) -> List[int]:
    ciphers: List[int] = []
    k = 2
    while k < m:
        flag = 1
        h = 2
        while h < k:
            if (k // h) * h == k:
                flag = 0
                break
            h += 1
        if flag == 1:
            ciphers.append(k)
        k += 1
    return ciphers