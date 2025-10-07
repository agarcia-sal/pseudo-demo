from typing import List, Tuple


def get_max_triples(integer_n: int) -> int:
    sequence_S: List[int] = [(p * p) - p + 1 for p in range(1, integer_n + 1)]
    collection_result: List[Tuple[int, int, int]] = []

    for pos_x in range(integer_n - 2):
        for pos_y in range(pos_x + 1, integer_n - 1):
            for pos_z in range(pos_y + 1, integer_n):
                total_sum = sequence_S[pos_x] + sequence_S[pos_y] + sequence_S[pos_z]
                if total_sum % 3 == 0:
                    collection_result.append((sequence_S[pos_x], sequence_S[pos_y], sequence_S[pos_z]))

    return len(collection_result)