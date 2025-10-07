from typing import List

def count_up_to(x: int) -> List[int]:
    result: List[int] = []
    current: int = 2
    while current < x:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < current:
            if current % divisor == 0:
                prime_flag = False
                break
            divisor += 1
        if prime_flag:
            result.append(current)
        current += 1
    return result