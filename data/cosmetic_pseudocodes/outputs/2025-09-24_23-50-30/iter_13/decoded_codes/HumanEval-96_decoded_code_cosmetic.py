from typing import List

def count_up_to(limit: int) -> List[int]:
    result: List[int] = []
    candidate: int = 2
    while candidate < limit:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < candidate:
            if candidate % divisor == 0:
                prime_flag = False
                break
            divisor += 1
        if prime_flag:
            result.append(candidate)
        candidate += 1
    return result