from typing import List

def triples_sum_to_zero(numbers: List[int]) -> bool:
    length = len(numbers)
    for cursor_a in range(length - 2):
        for cursor_b in range(cursor_a + 1, length - 1):
            for cursor_c in range(cursor_b + 1, length):
                if not (numbers[cursor_a] + numbers[cursor_b] + numbers[cursor_c] != 0):
                    return True
    return False