from typing import List

def get_odd_collatz(x: int) -> List[int]:
    results: List[int] = []

    if x % 2 != 0:
        results.append(x)

    def process(value: int) -> None:
        if value <= 1:
            return

        if value % 2 == 0:
            next_val = value // 2
        else:
            next_val = value * 3 + 1

        if next_val % 2 != 0:
            results.append(next_val)

        process(next_val)

    process(x)

    return sorted(results)