from typing import List, Tuple


def get_max_triples(integer_n: int) -> int:
    list_A: List[int] = [(i * i) - i + 1 for i in range(1, integer_n + 1)]
    list_ans: List[Tuple[int, int, int]] = []
    for first_idx in range(integer_n - 2):
        for second_idx in range(first_idx + 1, integer_n - 1):
            for third_idx in range(second_idx + 1, integer_n):
                total_sum = (
                    list_A[first_idx] + list_A[second_idx] + list_A[third_idx]
                )
                if total_sum % 3 == 0:
                    list_ans.append(
                        (list_A[first_idx], list_A[second_idx], list_A[third_idx])
                    )
    return len(list_ans)