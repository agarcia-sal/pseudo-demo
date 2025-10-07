from typing import List


def count_up_to(n: int) -> List[int]:
    result: List[int] = []
    current: int = 2

    while current < n:
        divisor: int = 2
        prime_flag: bool = True

        while True:
            if divisor >= current:
                break
            if current - (current // divisor) * divisor == 0:
                prime_flag = False
                break
            divisor += 1

        if prime_flag:
            result.append(current)

        current += 1

    return result