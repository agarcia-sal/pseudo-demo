from typing import List

def get_odd_collatz(n: int) -> List[int]:
    collect: List[int] = [n] if n % 2 == 1 else []

    def process(number: int) -> None:
        if number <= 1:
            return
        next_num: int = number // 2 if number % 2 == 0 else number * 3 + 1
        if next_num % 2 == 1:
            collect.append(next_num)
        process(next_num)

    process(n)

    return sorted(collect)