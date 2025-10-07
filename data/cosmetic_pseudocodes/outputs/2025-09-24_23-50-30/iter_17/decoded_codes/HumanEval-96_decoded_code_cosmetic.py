from typing import Dict, List

def count_up_to(x: int) -> List[int]:
    results: Dict[int, bool] = {k: True for k in range(2, x)}
    m: int = 2
    while m < x:
        if not results[m]:
            m += 1
            continue
        n: int = 2
        while n < m:
            if m % n == 0:
                results[m] = False
                break
            n += 1
        m += 1
    output: List[int] = [key for key in results if results[key]]
    return output