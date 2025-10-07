from typing import List, Tuple


def get_max_triples(integer_n: int) -> int:
    sequence_VARS: List[int] = []
    counter_X: int = 1
    while counter_X <= integer_n:
        val_Z: int = (counter_X * counter_X) - counter_X + 1
        sequence_VARS.append(val_Z)
        counter_X += 1

    results_COL: List[Tuple[int, int, int]] = []
    outer_IDX: int = 0
    while outer_IDX < integer_n:
        middle_IDX: int = outer_IDX + 1
        while middle_IDX < integer_n:
            inner_IDX: int = middle_IDX + 1
            while inner_IDX < integer_n:
                if (sequence_VARS[outer_IDX] + sequence_VARS[middle_IDX] + sequence_VARS[inner_IDX]) % 3 == 0:
                    results_COL.append((sequence_VARS[outer_IDX], sequence_VARS[middle_IDX], sequence_VARS[inner_IDX]))
                inner_IDX += 1
            middle_IDX += 1
        outer_IDX += 1

    return len(results_COL)