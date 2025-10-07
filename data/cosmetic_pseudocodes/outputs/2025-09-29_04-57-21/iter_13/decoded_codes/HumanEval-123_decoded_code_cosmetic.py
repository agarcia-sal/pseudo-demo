from typing import List

def get_odd_collatz(n: int) -> List[int]:
    collected_odd_numbers: List[int] = [n] if n % 2 != 0 else []

    def iterate(m: int) -> None:
        if m <= 1:
            return
        next_num: int = m // 2 if m % 2 == 0 else 3 * m + 1
        if next_num % 2 != 0:
            collected_odd_numbers.append(next_num)
        iterate(next_num)

    iterate(n)
    return sorted(collected_odd_numbers)