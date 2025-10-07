from typing import List


def count_up_to(m: int) -> List[int]:
    discovered_numbers: List[int] = []

    def check_divisor(current: int, divisor: int) -> bool:
        if divisor * divisor > current:
            return True
        if current % divisor == 0:
            return False
        return check_divisor(current, divisor + 1)

    step = 2
    while step < m:
        if check_divisor(step, 2):
            discovered_numbers.append(step)
        step += 1

    return discovered_numbers