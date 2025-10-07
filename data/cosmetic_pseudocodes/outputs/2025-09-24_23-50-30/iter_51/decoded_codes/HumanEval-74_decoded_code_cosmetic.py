from typing import List, Sequence, Union


def total_match(x_list: Sequence[str], y_list: Sequence[str]) -> Union[Sequence[str], Sequence[str]]:
    def sum_lengths(idx: int, coll: Sequence[str], acc: int) -> int:
        if idx >= len(coll):
            return acc
        else:
            return sum_lengths(idx + 1, coll, acc + len(coll[idx]))

    x_total: int = sum_lengths(0, x_list, 0)
    y_total: int = sum_lengths(0, y_list, 0)
    return x_list if x_total <= y_total else y_list