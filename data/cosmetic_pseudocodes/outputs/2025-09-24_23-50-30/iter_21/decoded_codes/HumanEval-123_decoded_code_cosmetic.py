from typing import List


def get_odd_collatz(number: int) -> List[int]:
    def process_step(x: int, acc: List[int]) -> List[int]:
        if x == 1:
            return acc
        if x % 2 == 0:
            x //= 2
        else:
            x = 3 * x + 1
        if x % 2 == 1:
            acc.append(int(x))
        return process_step(x, acc)

    sequence: List[int] = [number] if number % 2 == 1 else []
    result_sequence = process_step(number, sequence)
    sorted_sequence: List[int] = []
    while result_sequence:
        max_val = result_sequence[0]
        for elem in result_sequence:
            if elem > max_val:
                max_val = elem
        sorted_sequence = [max_val] + sorted_sequence
        result_sequence = [item for item in result_sequence if item != max_val]
    return sorted_sequence