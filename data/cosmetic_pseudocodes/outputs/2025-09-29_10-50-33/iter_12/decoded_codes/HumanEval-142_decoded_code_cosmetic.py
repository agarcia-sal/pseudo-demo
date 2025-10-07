from typing import Sequence, Union

def sum_squares(input_collection: Sequence[int]) -> int:
    acc_container: list[int] = []

    def iterate(pos: int) -> None:
        if pos >= len(input_collection):
            return
        if pos % 3 != 0 and pos % 4 == 0:
            acc_container.append(input_collection[pos] ** 3)
        elif pos % 3 == 0:
            acc_container.append(input_collection[pos] * input_collection[pos])
        else:
            acc_container.append(input_collection[pos])
        iterate(pos + 1)

    iterate(0)
    return sum(acc_container)