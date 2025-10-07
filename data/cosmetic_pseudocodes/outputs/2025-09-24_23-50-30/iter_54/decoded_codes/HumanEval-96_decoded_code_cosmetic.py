from typing import List

def count_up_to(m: int) -> List[int]:
    result: List[int] = []
    index: int = 2
    while index < m:
        prime_flag: bool = True
        divisor: int = 2
        while divisor < index and prime_flag:
            if index % divisor == 0:
                prime_flag = False
                divisor = index  # exit loop
            divisor += 1
        if prime_flag:
            result.append(index)
        index += 1
    return result