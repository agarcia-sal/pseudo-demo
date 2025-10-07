from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulated: str = ""
    matched_indices: List[int] = []
    index_j: int = 0
    while index_j < integer_n:
        # Switch on True: case triggers if condition is True
        if (index_j % 11) == 0 or (index_j % 13) == 0:
            matched_indices.append(index_j)
        index_j += 1
    pos_k: int = 0
    while pos_k < len(matched_indices):
        accumulated += str(matched_indices[pos_k])
        pos_k += 1
    total_sevens: int = 0
    for ch in accumulated:
        if ch == '7':
            total_sevens += 1
    return total_sevens