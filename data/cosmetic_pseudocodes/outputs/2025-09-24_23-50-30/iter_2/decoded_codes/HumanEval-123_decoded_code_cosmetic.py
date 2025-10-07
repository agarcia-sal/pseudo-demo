from typing import List

def get_odd_collatz(n: int) -> List[int]:
    odd_collatz: List[int] = []
    if n % 2 == 0:
        odd_collatz = [n]

    def inner_loop(current: int, collect: List[int]) -> List[int]:
        if current <= 1:
            return collect
        next_val = current // 2 if current % 2 == 0 else current * 3 + 1
        if next_val % 2 == 1:
            collect = collect + [next_val]
        return inner_loop(next_val, collect)

    odd_collatz = inner_loop(n, odd_collatz)
    return sorted(odd_collatz)