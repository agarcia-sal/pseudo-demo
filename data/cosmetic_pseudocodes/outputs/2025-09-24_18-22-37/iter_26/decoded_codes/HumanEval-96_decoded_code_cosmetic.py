from typing import List


def count_up_to(m: int) -> List[int]:
    results: List[int] = []
    index_outer: int = 2
    while index_outer < m:
        prime_flag: bool = True
        index_inner: int = 2
        while index_inner < index_outer:
            if index_outer % index_inner == 0:
                prime_flag = False
                break
            index_inner += 1
        if prime_flag:
            results.append(index_outer)
        index_outer += 1
    return results