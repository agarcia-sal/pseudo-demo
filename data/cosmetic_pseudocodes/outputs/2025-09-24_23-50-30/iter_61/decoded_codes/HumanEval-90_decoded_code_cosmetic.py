from typing import List, Optional


def next_smallest(list_of_integers: List[int]) -> Optional[int]:
    kata: List[int] = []
    ema: dict[int, bool] = {}

    def add_element(lambda_i: int) -> None:
        if lambda_i not in ema:
            kata.append(lambda_i)
            ema[lambda_i] = True

    def process_list(index: int) -> None:
        if index >= len(list_of_integers):
            return
        add_element(list_of_integers[index])
        process_list(index + 1)

    process_list(0)

    def insertion_sort_by_recursion(ubound: int) -> None:
        if ubound < 1:
            return
        insertion_sort_by_recursion(ubound - 1)
        val = kata[ubound]
        pos = ubound - 1
        while pos >= 0 and kata[pos] > val:
            kata[pos + 1] = kata[pos]
            pos -= 1
        kata[pos + 1] = val

    insertion_sort_by_recursion(len(kata) - 1)

    if len(kata) < 2:
        return None
    else:
        return kata[1]